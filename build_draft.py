from __future__ import annotations

import ast
import inspect
import json
import types
from pathlib import Path
from typing import Any

import tensorstore as ts
from collections import OrderedDict
import importlib_metadata


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
    bodies = _split_statements(body)
    for file, body in bodies.items():
        (draft_dir / file).write_text(
            ast.unparse(
                ast.Module(
                    body=body,
                    type_ignores=[],
                ),
            )
        )

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


def _split_statements(statements: list[ast.AST]) -> dict[str, list[ast.AST]]:
    bodies = {
        "_tensorstore.pyi": ast.parse(
            """\
from typing import Optional, Tuple, Any, Union, Sequence, List, Callable, Literal, TypeAlias
from numbers import Real
import numpy
import numpy.typing
import asyncio

# _bool:TypeAlias = bool

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


def _parse_func(key: str, statement: Any) -> dict:
    name = _process_func_decleration(statement.__doc__.splitlines()[0])
    definition = f"def {name}: ..."
    return {
        "type": "function",
        "definition": definition,
        "ast": ast.parse(definition).body[0],
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
    return {
        "ast": ast.parse(f"{key} = {statement}").body[0],
        "type": type_name,
        "definition": str(statement),
        "doc": statement.__doc__,
    }


def parse_statement(key: str, statement: Any) -> dict:
    # if isinstance(statement, (types.BuiltinFunctionType, types.FunctionType)):
    if inspect.ismethod(statement):
        if statement.__doc__ is not None:
            return _parse_func(key, statement)
        else:
            return _parse_unknown(key, statement, type_name="unknown_mwrhod")
    elif isinstance(statement, type):
        if statement.__doc__ is not None:
            children_statements = [
                parse_statement(key, getattr(statement, key))
                for key in dir(statement)
                if not key.startswith("__") and key not in ("__init__",)
            ]
            # Filter out None
            children_statements = [
                child_stmt
                for child_stmt in children_statements
                if child_stmt is not None
            ]
            body = [
                child_stmt["ast"]
                for child_stmt in children_statements
                if "ast" in child_stmt
            ]
            if len(body) == 0:
                body = [ast.Pass()]
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
