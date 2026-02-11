from __future__ import annotations

import ast
import inspect
import json
import types
from cgi import parse
from collections import OrderedDict
from pathlib import Path
from typing import Any

import black
import importlib_metadata
import tensorstore as ts
from numpy.f2py.crackfortran import c
from numpy.lib.recfunctions import recursive_fill_fields


def main():
    ts_version = importlib_metadata.version("tensorstore")

    work_dir = Path(__file__).parent

    draft_dir = work_dir / "tensorstore-stubs-draft"
    draft_dir.mkdir(exist_ok=True)
    statements = OrderedDict({})
    for key in dir(ts):
        if key.startswith("_"):
            continue
        statement = getattr(ts, key)
        print(statement)
        result = parse_statement(key, statement)
        if result is None:
            continue
        statements[key] = result

    body = [stmt["ast"] for stmt in statements.values()]
    body = sort_body(body)

    bodies = _split_statements(body)
    for file, body in bodies.items():
        code = ast.unparse(
            ast.Module(
                body=body,
                type_ignores=[],
            ),
        )
        # Remove tensorstore. prefix from all definitions
        # TODO: Better way to handle on AST level
        code = code.replace("tensorstore.", "")
        code = code.replace("NoneType", "None")
        code = code.replace("ellipsis", "...")
        # write to file
        code = black.format_str(code, mode=black.Mode())
        (draft_dir / file).write_text(code)

    def wrap(values: dict) -> dict:
        if "children" in values:
            values["children"] = [wrap(child) for child in values["children"]]
        if "ast" not in values:
            return values
        values["ast"] = ast.dump(values["ast"])
        return values

    (draft_dir / f"_tensorstore.{ts_version}.json").write_text(
        json.dumps(
            {key: wrap(values) for key, values in statements.items()},
            indent=4,
            sort_keys=True,
        )
    )


def sort_body(body: list[ast.AST]) -> list[ast.AST]:
    # Sort the body by type and then by name
    def get_key(stmt: ast.AST):
        if isinstance(stmt, ast.FunctionDef):
            return f"1{stmt.name}"
        elif isinstance(stmt, ast.ClassDef):
            return f"0{stmt.name}"
        elif isinstance(stmt, ast.AnnAssign):
            return f"2{stmt.target.id if isinstance(stmt.target, ast.Name) else ''}"
        else:
            return "3"

    return list(sorted(body, key=get_key))


def _split_statements(statements: list[ast.AST]) -> dict[str, list[ast.AST]]:
    bodies = {
        "_tensorstore.pyi": ast.parse(
            """\
import typing
from typing import Optional, Tuple, Any, Union, Sequence, List, Callable, Literal, TypeAlias, ForwardRef, Any 
import collections.abc
from numbers import Real
import numbers
import numpy
import numpy.typing
import asyncio
import builtins


class _DimSelection:
    pass

_Feature = Any
"""
        ).body,
    }

    for stmt in statements:
        bodies["_tensorstore.pyi"].append(stmt)
    return bodies


def _process_func_decleration(name: str) -> str:
    name = name.replace("tensorstore.", "")
    # name = name.replace("bool", "_bool")
    return name


def _recurse_replace(annotation: ast.AST) -> ast.AST:
    # Special cases
    if getattr(annotation, "id", "") == "bool":
        # Replace bool with builtins.bool
        annotation.id = "builtins.bool"
    elif getattr(annotation, "id", "") == "ellipsis":
        # Replace NoneType with None
        annotation.id = "..."
    elif getattr(annotation, "id", "") == "numpy.ndarray":
        annotation.id = "numpy.typing.ArrayLike"
    # Standard cases

    elif isinstance(annotation, ast.Subscript):
        annotation.slice = _recurse_replace(annotation.slice)
    elif isinstance(annotation, ast.Tuple):
        annotation.elts = [_recurse_replace(elt) for elt in annotation.elts]
    return annotation


def _parse_func(key: str, statement: Any) -> dict:
    try:
        name = _process_func_decleration(statement.__doc__.splitlines()[0])
        definition = f"def {name}: ..."
        parsed_ast: ast.FunctionDef = ast.parse(definition).body[0]
    except Exception:
        # Sometimes functiuon docstring is not possible to parse directly
        if key == "__init__":
            # Special case for __init__
            parsed_ast = ast.parse(f"def {key}(self): ...").body[0]
        else:
            raise
    # Special case for bool annotation replacement
    for arg in parsed_ast.args.args:
        arg.annotation = _recurse_replace(arg.annotation)
    for arg in parsed_ast.args.kwonlyargs:
        arg.annotation = _recurse_replace(arg.annotation)
    for arg in parsed_ast.args.posonlyargs:
        arg.annotation = _recurse_replace(arg.annotation)
    if parsed_ast.returns is not None:
        parsed_ast.returns = _recurse_replace(parsed_ast.returns)
    return {
        "type": "function",
        "definition": definition,
        "ast": parsed_ast,
        "doc": statement.__doc__,
    }


def _parse_property(key: str, statement: Any) -> dict:
    part_stmt: str = statement.fget.__doc__.strip()
    if part_stmt.startswith(key):
        name = _process_func_decleration(statement.fget.__doc__.strip())
        definition = "@property\n" + "def " + name + ": ..."
    else:
        name = _process_func_decleration(statement.fget.__doc__.strip())
        definition = "@property\n" + "def " + key + " " + name + ": ..."
    return {
        "type": "property",
        "ast": ast.parse(definition).body[0],
        "definition": definition,
        "doc": statement.__doc__,
    }


def _parse_unknown(key: str, statement: Any, type_name="unknown") -> dict:
    if key == "T":
        return {
            "ast": ast.parse(f"T:Any =...").body[0],
            "type": type_name,
            "definition": str(statement),
            "doc": statement.__doc__,
        }

    try:
        # A case of alias type or constant value
        parsed_ast = ast.parse(f"{key} = {statement}").body[0]
    except Exception:
        # Assuming statement is directly not parsable
        return {
            "ast": ast.parse(f'{key}:"{type(statement).__name__}" = ...').body[0],
            "type": type_name,
            "definition": str(statement),
            "doc": statement.__doc__,
        }

    parsed_ast = _recurse_replace(parsed_ast)
    return {
        "ast": parsed_ast,
        "type": type_name,
        "definition": str(statement),
        "doc": statement.__doc__,
    }


def _parse_class(key: str, statement: Any) -> dict:

    children_statements = [
        parse_statement(field_name, getattr(statement, field_name))
        for field_name in dir(statement)
        if not field_name.startswith("__") or field_name in ("__init__",)
    ]
    # Filter out None
    children_statements = [
        child_stmt for child_stmt in children_statements if child_stmt is not None
    ]
    body = [
        child_stmt["ast"] for child_stmt in children_statements if "ast" in child_stmt
    ]
    if len(body) == 0:
        body = [ast.Pass()]

    # Special case for `dtype` class
    if key == "dtype":
        body.insert(
            0,
            ast.parse("def __init__(self, dtype:str): ...").body[0],
        )
    return {
        "type": "class",
        "ast": ast.ClassDef(
            name=key,
            bases=[],
            keywords=[],
            body=body,
            decorator_list=[],
        ),
        "definition": str(statement),
        "doc": statement.__doc__,
        "children": children_statements,
    }


def parse_statement(key: str, statement: Any) -> dict:
    # if isinstance(statement, (types.BuiltinFunctionType, types.FunctionType)):
    if inspect.ismethod(statement):
        if statement.__doc__ is not None:
            return _parse_func(key, statement)
        else:
            return _parse_unknown(key, statement, type_name="unknown_method")
    elif isinstance(statement, type):
        if statement.__doc__ is not None:
            return _parse_class(key, statement)
        else:
            return {
                "type": "unknown_type",
                "definition": str(statement),
                "doc": statement.__doc__,
            }
    elif isinstance(statement, types.ModuleType):
        return None
    elif isinstance(statement, property):
        return _parse_property(key, statement)
    else:
        if (
            callable(statement)
            and hasattr(statement, "__doc__")
            and statement.__doc__ is not None
            and statement.__doc__.splitlines()[0] != ""
        ):
            # Maybe instantce method
            return _parse_func(key, statement)
        else:
            # Maybe value
            if key.startswith("_"):
                # No need to generate stub for private variable
                return None
            return _parse_unknown(key, statement)


if __name__ == "__main__":
    main()
