import asyncio
import builtins
import collections.abc
import numbers
import typing
from numbers import Real
from typing import (
    Any,
    Callable,
    ForwardRef,
    List,
    Literal,
    Optional,
    Sequence,
    Tuple,
    TypeAlias,
    Union,
)

import numpy
import numpy.typing

class _DimSelection:
    pass

_Feature = Any

class Batch:
    def __init__(self: Batch) -> None: ...
    def submit(self: Batch) -> None: ...

class ChunkLayout:
    class Grid:
        def __init__(*args, **kwargs): ...
        @property
        def aspect_ratio(
            arg0: ChunkLayout.Grid,
        ) -> Optional[Tuple[Optional[float], ...]]: ...
        @property
        def aspect_ratio_soft_constraint(
            arg0: ChunkLayout.Grid,
        ) -> Optional[Tuple[Optional[float], ...]]: ...
        @property
        def elements(arg0: ChunkLayout.Grid) -> Optional[int]: ...
        @property
        def elements_soft_constraint(arg0: ChunkLayout.Grid) -> Optional[int]: ...
        @property
        def ndim(arg0: ChunkLayout.Grid) -> Optional[int]: ...
        @property
        def rank(arg0: ChunkLayout.Grid) -> Optional[int]: ...
        @property
        def shape(arg0: ChunkLayout.Grid) -> Optional[Tuple[Optional[int], ...]]: ...
        @property
        def shape_soft_constraint(
            arg0: ChunkLayout.Grid,
        ) -> Optional[Tuple[Optional[int], ...]]: ...
        def to_json(
            self: ChunkLayout.Grid, include_defaults: builtins.bool = False
        ) -> Any: ...
        def update(
            self: ChunkLayout.Grid,
            *,
            rank: Optional[int] = None,
            shape: Optional[collections.abc.Iterable[Optional[int]]] = None,
            shape_soft_constraint: Optional[
                collections.abc.Iterable[Optional[int]]
            ] = None,
            aspect_ratio: Optional[collections.abc.Iterable[Optional[float]]] = None,
            aspect_ratio_soft_constraint: Optional[
                collections.abc.Iterable[Optional[float]]
            ] = None,
            elements: Optional[int] = None,
            elements_soft_constraint: Optional[int] = None,
            grid: Optional[ChunkLayout.Grid] = None,
            grid_soft_constraint: Optional[ChunkLayout.Grid] = None,
        ) -> None: ...

    def __init__(*args, **kwargs): ...
    @property
    def codec_chunk(arg0: ChunkLayout) -> ChunkLayout.Grid: ...
    @property
    def grid_origin(arg0: ChunkLayout) -> Optional[Tuple[Optional[int], ...]]: ...
    @property
    def grid_origin_soft_constraint(
        arg0: ChunkLayout,
    ) -> Optional[Tuple[Optional[int], ...]]: ...
    @property
    def inner_order(arg0: ChunkLayout) -> Optional[Tuple[int, ...]]: ...
    @property
    def inner_order_soft_constraint(arg0: ChunkLayout) -> Optional[Tuple[int, ...]]: ...
    @property
    def ndim(arg0: ChunkLayout) -> int: ...
    @property
    def rank(arg0: ChunkLayout) -> int: ...
    @property
    def read_chunk(arg0: ChunkLayout) -> ChunkLayout.Grid: ...
    @property
    def read_chunk_template(arg0: ChunkLayout) -> IndexDomain: ...
    def to_json(self: ChunkLayout) -> Any: ...
    def update(
        self: ChunkLayout,
        *,
        rank: Optional[int] = None,
        inner_order: Optional[collections.abc.Iterable[int]] = None,
        inner_order_soft_constraint: Optional[collections.abc.Iterable[int]] = None,
        grid_origin: Optional[collections.abc.Iterable[Optional[int]]] = None,
        grid_origin_soft_constraint: Optional[
            collections.abc.Iterable[Optional[int]]
        ] = None,
        chunk: Optional[ChunkLayout.Grid] = None,
        write_chunk: Optional[ChunkLayout.Grid] = None,
        read_chunk: Optional[ChunkLayout.Grid] = None,
        codec_chunk: Optional[ChunkLayout.Grid] = None,
        chunk_shape: Optional[collections.abc.Iterable[Optional[int]]] = None,
        chunk_shape_soft_constraint: Optional[
            collections.abc.Iterable[Optional[int]]
        ] = None,
        write_chunk_shape: Optional[collections.abc.Iterable[Optional[int]]] = None,
        write_chunk_shape_soft_constraint: Optional[
            collections.abc.Iterable[Optional[int]]
        ] = None,
        read_chunk_shape: Optional[collections.abc.Iterable[Optional[int]]] = None,
        read_chunk_shape_soft_constraint: Optional[
            collections.abc.Iterable[Optional[int]]
        ] = None,
        codec_chunk_shape: Optional[collections.abc.Iterable[Optional[int]]] = None,
        codec_chunk_shape_soft_constraint: Optional[
            collections.abc.Iterable[Optional[int]]
        ] = None,
        chunk_aspect_ratio: Optional[collections.abc.Iterable[Optional[float]]] = None,
        chunk_aspect_ratio_soft_constraint: Optional[
            collections.abc.Iterable[Optional[float]]
        ] = None,
        write_chunk_aspect_ratio: Optional[
            collections.abc.Iterable[Optional[float]]
        ] = None,
        write_chunk_aspect_ratio_soft_constraint: Optional[
            collections.abc.Iterable[Optional[float]]
        ] = None,
        read_chunk_aspect_ratio: Optional[
            collections.abc.Iterable[Optional[float]]
        ] = None,
        read_chunk_aspect_ratio_soft_constraint: Optional[
            collections.abc.Iterable[Optional[float]]
        ] = None,
        codec_chunk_aspect_ratio: Optional[
            collections.abc.Iterable[Optional[float]]
        ] = None,
        codec_chunk_aspect_ratio_soft_constraint: Optional[
            collections.abc.Iterable[Optional[float]]
        ] = None,
        chunk_elements: Optional[int] = None,
        chunk_elements_soft_constraint: Optional[int] = None,
        write_chunk_elements: Optional[int] = None,
        write_chunk_elements_soft_constraint: Optional[int] = None,
        read_chunk_elements: Optional[int] = None,
        read_chunk_elements_soft_constraint: Optional[int] = None,
        codec_chunk_elements: Optional[int] = None,
        codec_chunk_elements_soft_constraint: Optional[int] = None,
        finalize: Optional[builtins.bool] = None,
    ) -> None: ...
    @property
    def write_chunk(arg0: ChunkLayout) -> ChunkLayout.Grid: ...
    @property
    def write_chunk_template(arg0: ChunkLayout) -> IndexDomain: ...

class CodecSpec:
    def __init__(self: CodecSpec, json: Any) -> None: ...
    def to_json(self: CodecSpec, include_defaults: builtins.bool = False) -> Any: ...

class Context:
    class Resource:
        def __init__(self): ...
        def to_json(
            self: Context.Resource, include_defaults: builtins.bool = False
        ) -> Any: ...

    class Spec:
        def __init__(self: Context.Spec, json: Any) -> None: ...
        def to_json(
            self: Context.Spec, include_defaults: builtins.bool = False
        ) -> Any: ...

    def __init__(*args, **kwargs): ...
    @property
    def parent(arg0: Context) -> Context: ...
    @property
    def spec(arg0: Context) -> Context.Spec: ...

class Dim:
    def __init__(*args, **kwargs): ...
    @property
    def empty(arg0: Dim) -> bool: ...
    @property
    def exclusive_max(arg0: Dim) -> int: ...
    @property
    def exclusive_min(arg0: Dim) -> int: ...
    @property
    def finite(arg0: Dim) -> bool: ...
    def hull(self: Dim, other: Dim) -> Dim: ...
    @property
    def implicit_lower(arg0: Dim) -> bool: ...
    @property
    def implicit_upper(arg0: Dim) -> bool: ...
    @property
    def inclusive_max(arg0: Dim) -> int: ...
    @property
    def inclusive_min(arg0: Dim) -> int: ...
    def intersect(self: Dim, other: Dim) -> Dim: ...
    @property
    def label(arg0: Dim) -> str: ...
    @property
    def size(arg0: Dim) -> int: ...

class DimExpression:
    def __init__(self): ...
    @property
    def diagonal(arg0: DimExpression) -> DimExpression: ...
    @property
    def label(arg0: object) -> DimExpression._Label: ...
    @property
    def mark_bounds_implicit(arg0: object) -> DimExpression._MarkBoundsImplicit: ...
    @property
    def oindex(arg0: object) -> DimExpression._Oindex: ...
    @property
    def stride(arg0: object) -> DimExpression._Stride: ...
    @property
    def translate_backward_by(arg0: object) -> DimExpression._TranslateBackwardBy: ...
    @property
    def translate_by(arg0: object) -> DimExpression._TranslateBy: ...
    @property
    def translate_to(arg0: object) -> DimExpression._TranslateTo: ...
    @property
    def transpose(arg0: object) -> DimExpression._Transpose: ...
    @property
    def vindex(arg0: object) -> DimExpression._Vindex: ...

class DimSelection:
    def __init__(self): ...
    @property
    def diagonal(arg0: DimExpression) -> DimExpression: ...
    @property
    def label(arg0: object) -> DimExpression._Label: ...
    @property
    def mark_bounds_implicit(arg0: object) -> DimExpression._MarkBoundsImplicit: ...
    @property
    def oindex(arg0: object) -> DimExpression._Oindex: ...
    @property
    def stride(arg0: object) -> DimExpression._Stride: ...
    @property
    def translate_backward_by(arg0: object) -> DimExpression._TranslateBackwardBy: ...
    @property
    def translate_by(arg0: object) -> DimExpression._TranslateBy: ...
    @property
    def translate_to(arg0: object) -> DimExpression._TranslateTo: ...
    @property
    def transpose(arg0: object) -> DimExpression._Transpose: ...
    @property
    def vindex(arg0: object) -> DimExpression._Vindex: ...

class Future:
    def __init__(self): ...
    def add_done_callback(
        self: Future, callback: Callable[[Future[T]], None]
    ) -> None: ...
    def cancel(self: Future) -> builtins.bool: ...
    def cancelled(self: Future) -> builtins.bool: ...
    def done(self: Future) -> builtins.bool: ...
    def exception(
        self: Future, timeout: Optional[float] = None, deadline: Optional[float] = None
    ) -> object: ...
    def force(self: Future) -> None: ...
    def remove_done_callback(
        self: Future, callback: Callable[[Future[T]], None]
    ) -> int: ...
    def result(
        self: Future, timeout: Optional[float] = None, deadline: Optional[float] = None
    ) -> T: ...

class IndexDomain:
    @property
    def T(arg0: IndexDomain) -> IndexDomain: ...
    def __init__(*args, **kwargs): ...
    @property
    def exclusive_max(arg0: IndexDomain) -> Tuple[int, ...]: ...
    def hull(self: IndexDomain, other: IndexDomain) -> IndexDomain: ...
    @property
    def implicit_lower_bounds(arg0: IndexDomain) -> Tuple[bool, ...]: ...
    @property
    def implicit_upper_bounds(arg0: IndexDomain) -> Tuple[bool, ...]: ...
    @property
    def inclusive_max(arg0: IndexDomain) -> Tuple[int, ...]: ...
    @property
    def inclusive_min(arg0: IndexDomain) -> Tuple[int, ...]: ...
    @property
    def index_exp(arg0: IndexDomain) -> Tuple[slice, ...]: ...
    def intersect(self: IndexDomain, other: IndexDomain) -> IndexDomain: ...
    @property
    def label(arg0: object) -> IndexDomain._Label: ...
    @property
    def labels(arg0: IndexDomain) -> Tuple[str, ...]: ...
    @property
    def mark_bounds_implicit(arg0: object) -> IndexDomain._MarkBoundsImplicit: ...
    @property
    def ndim(arg0: IndexDomain) -> int: ...
    @property
    def origin(arg0: IndexDomain) -> Tuple[int, ...]: ...
    @property
    def rank(arg0: IndexDomain) -> int: ...
    @property
    def shape(arg0: IndexDomain) -> Tuple[int, ...]: ...
    @property
    def size(arg0: IndexDomain) -> int: ...
    def to_json(self: IndexDomain) -> Any: ...
    @property
    def translate_backward_by(arg0: object) -> IndexDomain._TranslateBackwardBy: ...
    @property
    def translate_by(arg0: object) -> IndexDomain._TranslateBy: ...
    @property
    def translate_to(arg0: object) -> IndexDomain._TranslateTo: ...
    def transpose(
        self: IndexDomain, axes: Optional[DimSelectionLike] = None
    ) -> IndexDomain: ...

class IndexTransform:
    @property
    def T(arg0: IndexTransform) -> IndexTransform: ...
    def __init__(*args, **kwargs): ...
    @property
    def domain(arg0: IndexTransform) -> IndexDomain: ...
    @property
    def implicit_lower_bounds(arg0: IndexTransform) -> Tuple[bool, ...]: ...
    @property
    def implicit_upper_bounds(arg0: IndexTransform) -> Tuple[bool, ...]: ...
    @property
    def input_exclusive_max(arg0: IndexTransform) -> Tuple[int, ...]: ...
    @property
    def input_inclusive_max(arg0: IndexTransform) -> Tuple[int, ...]: ...
    @property
    def input_inclusive_min(arg0: IndexTransform) -> Tuple[int, ...]: ...
    @property
    def input_labels(arg0: IndexTransform) -> Tuple[str, ...]: ...
    @property
    def input_origin(arg0: IndexTransform) -> Tuple[int, ...]: ...
    @property
    def input_rank(arg0: IndexTransform) -> int: ...
    @property
    def input_shape(arg0: IndexTransform) -> Tuple[int, ...]: ...
    @property
    def label(arg0: object) -> IndexTransform._Label: ...
    @property
    def mark_bounds_implicit(arg0: object) -> IndexTransform._MarkBoundsImplicit: ...
    @property
    def ndim(arg0: IndexTransform) -> int: ...
    @property
    def oindex(arg0: object) -> IndexTransform._Oindex: ...
    @property
    def origin(arg0: IndexTransform) -> Tuple[int, ...]: ...
    @property
    def output(arg0: IndexTransform) -> OutputIndexMaps: ...
    @property
    def output_rank(arg0: IndexTransform) -> int: ...
    @property
    def shape(arg0: IndexTransform) -> Tuple[int, ...]: ...
    @property
    def size(arg0: IndexTransform) -> int: ...
    def to_json(self: IndexTransform) -> Any: ...
    @property
    def translate_backward_by(arg0: object) -> IndexTransform._TranslateBackwardBy: ...
    @property
    def translate_by(arg0: object) -> IndexTransform._TranslateBy: ...
    @property
    def translate_to(arg0: object) -> IndexTransform._TranslateTo: ...
    def transpose(
        self: IndexTransform, axes: Optional[DimSelectionLike] = None
    ) -> IndexTransform: ...
    @property
    def vindex(arg0: object) -> IndexTransform._Vindex: ...

class Indexable:
    def __init__(self): ...

class KvStore:
    class KeyRange:
        def __init__(
            self: KvStore.KeyRange,
            inclusive_min: str | bytes = "",
            exclusive_max: str | bytes = "",
        ) -> None: ...
        def copy(self: KvStore.KeyRange) -> KvStore.KeyRange: ...
        @property
        def empty(arg0: KvStore.KeyRange) -> bool: ...
        @property
        def exclusive_max(arg0: KvStore.KeyRange) -> bytes: ...
        @property
        def inclusive_min(arg0: KvStore.KeyRange) -> bytes: ...

    class ReadResult:
        def __init__(
            self: KvStore.ReadResult,
            state: Literal["unspecified", "missing", "value"] = "unspecified",
            value: str | bytes = "",
            stamp: KvStore.TimestampedStorageGeneration = KvStore.TimestampedStorageGeneration(
                b"", -inf
            ),
        ) -> None: ...
        @property
        def stamp(arg0: KvStore.ReadResult) -> KvStore.TimestampedStorageGeneration: ...
        @property
        def state(
            arg0: KvStore.ReadResult,
        ) -> Literal["unspecified", "missing", "value"]: ...
        @property
        def value(arg0: KvStore.ReadResult) -> bytes: ...

    class Spec:
        def __init__(self): ...
        @property
        def base(arg0: KvStore.Spec) -> Optional[KvStore.Spec]: ...
        def copy(self: KvStore.Spec) -> KvStore.Spec: ...
        @property
        def path(arg0: KvStore.Spec) -> str: ...
        def to_json(
            self: KvStore.Spec, include_defaults: builtins.bool = False
        ) -> Any: ...
        def update(
            self: KvStore.Spec,
            *,
            unbind_context: Optional[builtins.bool] = None,
            strip_context: Optional[builtins.bool] = None,
            context: Optional[Context] = None,
        ) -> None: ...
        @property
        def url(arg0: KvStore.Spec) -> str: ...

    class TimestampedStorageGeneration:
        def __init__(
            self: KvStore.TimestampedStorageGeneration,
            generation: str | bytes = "",
            time: float = -inf,
        ) -> None: ...
        @property
        def generation(arg0: KvStore.TimestampedStorageGeneration) -> bytes: ...
        @property
        def time(arg0: KvStore.TimestampedStorageGeneration) -> float: ...

    def __init__(self): ...
    @property
    def base(arg0: KvStore) -> Optional[KvStore]: ...
    def copy(self: KvStore) -> KvStore: ...
    def delete_range(self: KvStore, range: KvStore.KeyRange) -> Future[None]: ...
    def experimental_copy_range_to(
        self: KvStore,
        target: KvStore,
        source_range: Optional[KvStore.KeyRange] = None,
        source_staleness_bound: Optional[float] = None,
    ) -> Future[None]: ...
    def list(
        self: KvStore,
        range: Optional[KvStore.KeyRange] = None,
        strip_prefix_length: int = 0,
    ) -> Future[List[bytes]]: ...
    def open(
        spec: Union[KvStore.Spec, Any],
        *,
        context: Optional[Context] = None,
        transaction: Optional[Transaction] = None,
    ) -> Future[KvStore]: ...
    @property
    def path(arg0: KvStore) -> str: ...
    def read(
        self: KvStore,
        key: str | bytes,
        *,
        if_not_equal: Optional[str | bytes] = None,
        staleness_bound: Optional[float] = None,
        batch: Optional[Batch] = None,
        byte_range: Optional[slice[Optional[int], Optional[int], None]] = None,
    ) -> Future[KvStore.ReadResult]: ...
    def spec(
        self: KvStore,
        *,
        retain_context: Optional[builtins.bool] = None,
        unbind_context: Optional[builtins.bool] = None,
    ) -> KvStore.Spec: ...
    @property
    def transaction(arg0: KvStore) -> Optional[Transaction]: ...
    @property
    def url(arg0: KvStore) -> str: ...
    def with_transaction(
        self: KvStore, transaction: Optional[Transaction]
    ) -> KvStore: ...
    def write(
        self: KvStore,
        key: str | bytes,
        value: Optional[str | bytes],
        *,
        if_equal: Optional[str | bytes] = None,
    ) -> Future[KvStore.TimestampedStorageGeneration]: ...

class OpenMode:
    def __init__(
        self: OpenMode,
        *,
        open: builtins.bool = False,
        create: builtins.bool = False,
        delete_existing: builtins.bool = False,
        assume_metadata: builtins.bool = False,
        assume_cached_metadata: builtins.bool = False,
    ) -> None: ...
    @property
    def assume_cached_metadata(arg0: OpenMode) -> bool: ...
    @property
    def assume_metadata(arg0: OpenMode) -> bool: ...
    @property
    def create(arg0: OpenMode) -> bool: ...
    @property
    def delete_existing(arg0: OpenMode) -> bool: ...
    @property
    def open(arg0: OpenMode) -> bool: ...

class OutputIndexMap:
    def __init__(*args, **kwargs): ...
    @property
    def index_array(arg0: OutputIndexMap) -> Optional[numpy.ndarray]: ...
    @property
    def index_range(arg0: OutputIndexMap) -> Optional[Dim]: ...
    @property
    def input_dimension(arg0: OutputIndexMap) -> Optional[int]: ...
    @property
    def method(arg0: OutputIndexMap) -> OutputIndexMethod: ...
    @property
    def offset(arg0: OutputIndexMap) -> int: ...
    @property
    def stride(arg0: OutputIndexMap) -> Optional[int]: ...

class OutputIndexMaps:
    def __init__(self): ...
    @property
    def rank(arg0: OutputIndexMaps) -> int: ...

class OutputIndexMethod:
    def __init__(self: OutputIndexMethod, value: int) -> None: ...

    array = OutputIndexMethod.array
    constant = OutputIndexMethod.constant

    @property
    def name(self: object, /) -> str: ...

    single_input_dimension = OutputIndexMethod.single_input_dimension

    @property
    def value(arg0: OutputIndexMethod) -> int: ...

class Promise:
    def __init__(self): ...
    def new() -> tuple[Promise[T], Future[T]]: ...
    def set_exception(self: Promise, exception: object) -> None: ...
    def set_result(self: Promise, result: T) -> None: ...

class Schema:
    @property
    def T(arg0: Schema) -> Schema: ...
    def __init__(*args, **kwargs): ...
    @property
    def chunk_layout(arg0: Schema) -> ChunkLayout: ...
    @property
    def codec(arg0: Schema) -> Optional[CodecSpec]: ...
    def copy(self: Schema) -> Schema: ...
    @property
    def dimension_units(arg0: Schema) -> Optional[Tuple[Optional[Unit], ...]]: ...
    @property
    def domain(arg0: Schema) -> Optional[IndexDomain]: ...
    @property
    def dtype(arg0: Schema) -> Optional[dtype]: ...
    @property
    def fill_value(arg0: Schema) -> Optional[numpy.ndarray]: ...
    @property
    def label(arg0: object) -> Schema._Label: ...
    @property
    def mark_bounds_implicit(arg0: object) -> Schema._MarkBoundsImplicit: ...
    @property
    def ndim(arg0: Schema) -> Optional[int]: ...
    @property
    def oindex(arg0: object) -> Schema._Oindex: ...
    @property
    def origin(arg0: Schema) -> Tuple[int, ...]: ...
    @property
    def rank(arg0: Schema) -> Optional[int]: ...
    @property
    def shape(arg0: Schema) -> Tuple[int, ...]: ...
    @property
    def size(arg0: Schema) -> int: ...
    def to_json(self: Schema, include_defaults: builtins.bool = False) -> Any: ...
    @property
    def translate_backward_by(arg0: object) -> Schema._TranslateBackwardBy: ...
    @property
    def translate_by(arg0: object) -> Schema._TranslateBy: ...
    @property
    def translate_to(arg0: object) -> Schema._TranslateTo: ...
    def transpose(self: Schema, axes: Optional[DimSelectionLike] = None) -> Schema: ...
    def update(
        self: Schema,
        *,
        rank: Optional[int] = None,
        dtype: Optional[DTypeLike] = None,
        domain: Optional[IndexDomain] = None,
        shape: Optional[collections.abc.Iterable[int]] = None,
        chunk_layout: Optional[ChunkLayout] = None,
        codec: Optional[CodecSpec] = None,
        fill_value: Optional[numpy.typing.ArrayLike] = None,
        dimension_units: Optional[
            collections.abc.Iterable[
                Optional[Union[Unit, str, numbers.Real, tuple[numbers.Real, str]]]
            ]
        ] = None,
        schema: Optional[Schema] = None,
    ) -> None: ...
    @property
    def vindex(arg0: object) -> Schema._Vindex: ...

class Spec:
    @property
    def T(arg0: Spec) -> Spec: ...
    def __init__(self): ...
    @property
    def base(arg0: Spec) -> Optional[Spec]: ...
    @property
    def chunk_layout(arg0: Spec) -> ChunkLayout: ...
    @property
    def codec(arg0: Spec) -> Optional[CodecSpec]: ...
    def copy(self: Spec) -> Spec: ...
    @property
    def dimension_units(arg0: Spec) -> Optional[Tuple[Optional[Unit], ...]]: ...
    @property
    def domain(arg0: Spec) -> Optional[IndexDomain]: ...
    @property
    def dtype(arg0: Spec) -> Optional[dtype]: ...
    @property
    def fill_value(arg0: Spec) -> Optional[numpy.ndarray]: ...
    @property
    def kvstore(arg0: Spec) -> Optional[KvStore.Spec]: ...
    @property
    def label(arg0: object) -> Spec._Label: ...
    @property
    def mark_bounds_implicit(arg0: object) -> Spec._MarkBoundsImplicit: ...
    @property
    def ndim(arg0: Spec) -> Optional[int]: ...
    @property
    def oindex(arg0: object) -> Spec._Oindex: ...
    @property
    def open_mode(arg0: Spec) -> OpenMode: ...
    @property
    def origin(arg0: Spec) -> Tuple[int, ...]: ...
    @property
    def rank(arg0: Spec) -> Optional[int]: ...
    @property
    def schema(arg0: Spec) -> Schema: ...
    @property
    def shape(arg0: Spec) -> Tuple[int, ...]: ...
    @property
    def size(arg0: Spec) -> int: ...
    def to_json(self: Spec, include_defaults: builtins.bool = False) -> Any: ...
    @property
    def transform(arg0: Spec) -> Optional[IndexTransform]: ...
    @property
    def translate_backward_by(arg0: object) -> Spec._TranslateBackwardBy: ...
    @property
    def translate_by(arg0: object) -> Spec._TranslateBy: ...
    @property
    def translate_to(arg0: object) -> Spec._TranslateTo: ...
    def transpose(self: Spec, axes: Optional[DimSelectionLike] = None) -> Spec: ...
    def update(
        self: Spec,
        *,
        open_mode: Optional[OpenMode] = None,
        open: Optional[builtins.bool] = None,
        create: Optional[builtins.bool] = None,
        delete_existing: Optional[builtins.bool] = None,
        assume_metadata: Optional[builtins.bool] = None,
        assume_cached_metadata: Optional[builtins.bool] = None,
        unbind_context: Optional[builtins.bool] = None,
        strip_context: Optional[builtins.bool] = None,
        context: Optional[Context] = None,
        kvstore: Optional[KvStore.Spec] = None,
        minimal_spec: Optional[builtins.bool] = None,
        recheck_cached_metadata: Optional[RecheckCacheOption] = None,
        recheck_cached_data: Optional[RecheckCacheOption] = None,
        recheck_cached: Optional[RecheckCacheOption] = None,
        rank: Optional[int] = None,
        dtype: Optional[DTypeLike] = None,
        domain: Optional[IndexDomain] = None,
        shape: Optional[collections.abc.Iterable[int]] = None,
        chunk_layout: Optional[ChunkLayout] = None,
        codec: Optional[CodecSpec] = None,
        fill_value: Optional[numpy.typing.ArrayLike] = None,
        dimension_units: Optional[
            collections.abc.Iterable[
                Optional[Union[Unit, str, numbers.Real, tuple[numbers.Real, str]]]
            ]
        ] = None,
        schema: Optional[Schema] = None,
    ) -> None: ...
    @property
    def url(arg0: Spec) -> str: ...
    @property
    def vindex(arg0: object) -> Spec._Vindex: ...

class TensorStore:
    class StorageStatistics:
        def __init__(
            self: TensorStore.StorageStatistics,
            *,
            not_stored: Optional[builtins.bool] = None,
            fully_stored: Optional[builtins.bool] = None,
        ) -> None: ...
        @property
        def fully_stored(arg0: TensorStore.StorageStatistics) -> Optional[bool]: ...
        @property
        def not_stored(arg0: TensorStore.StorageStatistics) -> Optional[bool]: ...

    @property
    def T(arg0: TensorStore) -> TensorStore: ...
    def __init__(self): ...
    def astype(self: TensorStore, dtype: DTypeLike) -> TensorStore: ...
    @property
    def base(arg0: TensorStore) -> Optional[TensorStore]: ...
    @property
    def chunk_layout(arg0: TensorStore) -> ChunkLayout: ...
    @property
    def codec(arg0: TensorStore) -> Optional[CodecSpec]: ...
    @property
    def dimension_units(arg0: TensorStore) -> Tuple[Optional[Unit], ...]: ...
    @property
    def domain(arg0: TensorStore) -> IndexDomain: ...
    @property
    def dtype(arg0: TensorStore) -> dtype: ...
    @property
    def fill_value(arg0: TensorStore) -> Optional[numpy.ndarray]: ...
    @property
    def kvstore(arg0: TensorStore) -> Optional[KvStore]: ...
    @property
    def label(arg0: object) -> TensorStore._Label: ...
    @property
    def mark_bounds_implicit(arg0: object) -> TensorStore._MarkBoundsImplicit: ...
    @property
    def mode(arg0: TensorStore) -> str: ...
    @property
    def ndim(arg0: TensorStore) -> int: ...
    @property
    def oindex(arg0: object) -> TensorStore._Oindex: ...
    @property
    def origin(arg0: TensorStore) -> Tuple[int, ...]: ...
    @property
    def rank(arg0: TensorStore) -> int: ...
    def read(
        self: TensorStore,
        *,
        order: Literal["C", "F"] = "C",
        batch: Optional[Batch] = None,
    ) -> Future[numpy.ndarray]: ...
    @property
    def readable(arg0: TensorStore) -> bool: ...
    def resize(
        self: TensorStore,
        inclusive_min: Optional[collections.abc.Iterable[Optional[int]]] = None,
        exclusive_max: Optional[collections.abc.Iterable[Optional[int]]] = None,
        resize_metadata_only: builtins.bool = False,
        resize_tied_bounds: builtins.bool = False,
        expand_only: builtins.bool = False,
        shrink_only: builtins.bool = False,
    ) -> Future[TensorStore]: ...
    def resolve(
        self: TensorStore,
        fix_resizable_bounds: builtins.bool = False,
        batch: Optional[Batch] = None,
    ) -> Future[TensorStore]: ...
    @property
    def schema(arg0: TensorStore) -> Schema: ...
    @property
    def shape(arg0: TensorStore) -> Tuple[int, ...]: ...
    @property
    def size(arg0: TensorStore) -> int: ...
    def spec(
        self: TensorStore,
        *,
        open_mode: Optional[OpenMode] = None,
        open: Optional[builtins.bool] = None,
        create: Optional[builtins.bool] = None,
        delete_existing: Optional[builtins.bool] = None,
        assume_metadata: Optional[builtins.bool] = None,
        assume_cached_metadata: Optional[builtins.bool] = None,
        minimal_spec: Optional[builtins.bool] = None,
        retain_context: Optional[builtins.bool] = None,
        unbind_context: Optional[builtins.bool] = None,
        recheck_cached_metadata: Optional[RecheckCacheOption] = None,
        recheck_cached_data: Optional[RecheckCacheOption] = None,
        recheck_cached: Optional[RecheckCacheOption] = None,
    ) -> Spec: ...
    def storage_statistics(
        self: TensorStore,
        *,
        query_not_stored: builtins.bool = False,
        query_fully_stored: builtins.bool = False,
    ) -> Future[TensorStore.StorageStatistics]: ...
    @property
    def transaction(arg0: TensorStore) -> Optional[Transaction]: ...
    @property
    def translate_backward_by(arg0: object) -> TensorStore._TranslateBackwardBy: ...
    @property
    def translate_by(arg0: object) -> TensorStore._TranslateBy: ...
    @property
    def translate_to(arg0: object) -> TensorStore._TranslateTo: ...
    def transpose(
        self: TensorStore, axes: Optional[DimSelectionLike] = None
    ) -> TensorStore: ...
    @property
    def url(arg0: TensorStore) -> str: ...
    @property
    def vindex(arg0: object) -> TensorStore._Vindex: ...
    def with_transaction(
        self: TensorStore, transaction: Optional[Transaction]
    ) -> TensorStore: ...
    @property
    def writable(arg0: TensorStore) -> bool: ...
    def write(
        self: TensorStore,
        source: Union[TensorStore, numpy.typing.ArrayLike],
        *,
        batch: Optional[Batch] = None,
        can_reference_source_data_indefinitely: Optional[builtins.bool] = None,
    ) -> WriteFutures: ...

class Transaction:
    def __init__(
        self: Transaction,
        atomic: builtins.bool = False,
        repeatable_read: builtins.bool = False,
    ) -> None: ...
    def abort(self: Transaction) -> None: ...
    @property
    def aborted(arg0: Transaction) -> bool: ...
    @property
    def atomic(arg0: Transaction) -> bool: ...
    def commit_async(self: Transaction) -> Future[None]: ...
    @property
    def commit_started(arg0: Transaction) -> bool: ...
    def commit_sync(self: Transaction) -> None: ...
    @property
    def future(arg0: Transaction) -> Future[None]: ...
    @property
    def open(arg0: Transaction) -> bool: ...

class Unit:
    def __init__(*args, **kwargs): ...
    @property
    def base_unit(arg0: Unit) -> str: ...
    @property
    def multiplier(arg0: Unit) -> float: ...
    def to_json(self: Unit) -> Any: ...

class VirtualChunkedReadParameters:
    def __init__(self): ...
    @property
    def batch(arg0: VirtualChunkedReadParameters) -> Optional[Batch]: ...
    @property
    def if_not_equal(arg0: VirtualChunkedReadParameters) -> bytes: ...
    @property
    def staleness_bound(arg0: VirtualChunkedReadParameters) -> float: ...

class VirtualChunkedWriteParameters:
    def __init__(self): ...
    @property
    def if_equal(arg0: VirtualChunkedWriteParameters) -> bytes: ...

class WriteFutures:
    def __init__(self): ...
    def add_done_callback(
        self: WriteFutures, callback: Callable[[Future], None]
    ) -> None: ...
    def cancel(self: WriteFutures) -> builtins.bool: ...
    def cancelled(self: WriteFutures) -> builtins.bool: ...
    @property
    def commit(arg0: WriteFutures) -> Future[None]: ...
    @property
    def copy(arg0: WriteFutures) -> Future[None]: ...
    def done(self: WriteFutures) -> builtins.bool: ...
    def exception(
        self: WriteFutures,
        timeout: Optional[float] = None,
        deadline: Optional[float] = None,
    ) -> object: ...
    def remove_done_callback(
        self: WriteFutures, callback: Callable[[Future], None]
    ) -> int: ...
    def result(
        self: WriteFutures,
        timeout: Optional[float] = None,
        deadline: Optional[float] = None,
    ) -> object: ...

class dtype:
    def __init__(self, dtype: str): ...
    def __init__(self: dtype, dtype: DTypeLike) -> None: ...
    @property
    def name(arg0: dtype) -> str: ...
    @property
    def numpy_dtype(arg0: dtype) -> numpy.dtype: ...
    def to_json(self: dtype) -> str: ...
    @property
    def type(arg0: dtype) -> type: ...

def array(
    array: numpy.typing.ArrayLike,
    dtype: Optional[DTypeLike] = None,
    *,
    context: Context = None,
    copy: Optional[builtins.bool] = None,
    write: Optional[builtins.bool] = None,
) -> TensorStore: ...
def cast(*args, **kwargs): ...
def concat(
    layers: collections.abc.Iterable[Union[TensorStore, Spec]],
    axis: Union[int, str],
    *,
    read: Optional[builtins.bool] = None,
    write: Optional[builtins.bool] = None,
    context: Optional[Context] = None,
    transaction: Optional[Transaction] = None,
    rank: Optional[int] = None,
    dtype: Optional[DTypeLike] = None,
    domain: Optional[IndexDomain] = None,
    shape: Optional[collections.abc.Iterable[int]] = None,
    dimension_units: Optional[
        collections.abc.Iterable[
            Optional[Union[Unit, str, numbers.Real, tuple[numbers.Real, str]]]
        ]
    ] = None,
    schema: Optional[Schema] = None,
) -> TensorStore: ...
def downsample(*args, **kwargs): ...
def experimental_collect_matching_metrics(
    metric_prefix: str = "", include_zero_metrics: builtins.bool = False
) -> list[Any]: ...
def experimental_collect_prometheus_format_metrics(
    metric_prefix: str = "",
) -> list[str]: ...
def experimental_push_metrics_to_prometheus(
    pushgateway: str = "", job: str = "", instance: str = "", metric_prefix: str = ""
) -> Future[int]: ...
def experimental_update_verbose_logging(
    flags: str = "", overwrite: builtins.bool = False
) -> None: ...
def open(
    spec: Union[Spec, Any],
    *,
    read: Optional[builtins.bool] = None,
    write: Optional[builtins.bool] = None,
    open_mode: Optional[OpenMode] = None,
    open: Optional[builtins.bool] = None,
    create: Optional[builtins.bool] = None,
    delete_existing: Optional[builtins.bool] = None,
    assume_metadata: Optional[builtins.bool] = None,
    assume_cached_metadata: Optional[builtins.bool] = None,
    context: Optional[Context] = None,
    transaction: Optional[Transaction] = None,
    batch: Optional[Batch] = None,
    kvstore: Optional[Union[KvStore.Spec, KvStore]] = None,
    recheck_cached_metadata: Optional[RecheckCacheOption] = None,
    recheck_cached_data: Optional[RecheckCacheOption] = None,
    recheck_cached: Optional[RecheckCacheOption] = None,
    rank: Optional[int] = None,
    dtype: Optional[DTypeLike] = None,
    domain: Optional[IndexDomain] = None,
    shape: Optional[collections.abc.Iterable[int]] = None,
    chunk_layout: Optional[ChunkLayout] = None,
    codec: Optional[CodecSpec] = None,
    fill_value: Optional[numpy.typing.ArrayLike] = None,
    dimension_units: Optional[
        collections.abc.Iterable[
            Optional[Union[Unit, str, numbers.Real, tuple[numbers.Real, str]]]
        ]
    ] = None,
    schema: Optional[Schema] = None,
) -> Future[TensorStore]: ...
def overlay(
    layers: collections.abc.Iterable[Union[TensorStore, Spec]],
    *,
    read: Optional[builtins.bool] = None,
    write: Optional[builtins.bool] = None,
    context: Optional[Context] = None,
    transaction: Optional[Transaction] = None,
    rank: Optional[int] = None,
    dtype: Optional[DTypeLike] = None,
    domain: Optional[IndexDomain] = None,
    shape: Optional[collections.abc.Iterable[int]] = None,
    dimension_units: Optional[
        collections.abc.Iterable[
            Optional[Union[Unit, str, numbers.Real, tuple[numbers.Real, str]]]
        ]
    ] = None,
    schema: Optional[Schema] = None,
) -> TensorStore: ...
def parse_tensorstore_flags(argv: list[str]) -> None: ...
def stack(
    layers: collections.abc.Iterable[Union[TensorStore, Spec]],
    axis: int = 0,
    *,
    read: Optional[builtins.bool] = None,
    write: Optional[builtins.bool] = None,
    context: Optional[Context] = None,
    transaction: Optional[Transaction] = None,
    rank: Optional[int] = None,
    dtype: Optional[DTypeLike] = None,
    domain: Optional[IndexDomain] = None,
    shape: Optional[collections.abc.Iterable[int]] = None,
    dimension_units: Optional[
        collections.abc.Iterable[
            Optional[Union[Unit, str, numbers.Real, tuple[numbers.Real, str]]]
        ]
    ] = None,
    schema: Optional[Schema] = None,
) -> TensorStore: ...
def virtual_chunked(
    read_function: Optional[
        Callable[
            [IndexDomain, numpy.ndarray, VirtualChunkedReadParameters],
            FutureLike[Optional[KvStore.TimestampedStorageGeneration]],
        ]
    ] = None,
    write_function: Optional[
        Callable[
            [IndexDomain, numpy.ndarray, VirtualChunkedWriteParameters],
            FutureLike[Optional[KvStore.TimestampedStorageGeneration]],
        ]
    ] = None,
    *,
    loop: Optional[asyncio.AbstractEventLoop] = None,
    rank: Optional[int] = None,
    dtype: Optional[DTypeLike] = None,
    domain: Optional[IndexDomain] = None,
    shape: Optional[collections.abc.Iterable[int]] = None,
    chunk_layout: Optional[ChunkLayout] = None,
    dimension_units: Optional[
        collections.abc.Iterable[
            Optional[Union[Unit, str, numbers.Real, tuple[numbers.Real, str]]]
        ]
    ] = None,
    schema: Optional[Schema] = None,
    context: Optional[Context] = None,
    transaction: Optional[Transaction] = None,
) -> TensorStore: ...

T: Any = ...
d: "_DimSelection" = ...
DTypeLike = typing.Union[ForwardRef("dtype"), str, type, ForwardRef("numpy.dtype")]
DimSelectionLike = typing.Union[
    DimSelection,
    typing.SupportsIndex,
    str,
    bytes,
    ForwardRef("slice[typing.SupportsIndex | None]"),
    collections.abc.Sequence["DimSelectionLike"],
]
DownsampleMethod = typing.Literal["stride", "median", "mode", "mean", "min", "max"]
FutureLike = typing.Union[Future[+T], collections.abc.Awaitable[+T], +T]
NumpyIndexTerm = typing.Union[
    typing.SupportsIndex,
    ForwardRef(
        "slice[typing.SupportsIndex | collections.abc.Sequence[typing.SupportsIndex | None] | None]"
    ),
    None,
    ...,
    ForwardRef("numpy.typing.ArrayLike"),
]
NumpyIndexingSpec = typing.Union[
    ForwardRef("NumpyIndexTerm"), tuple["NumpyIndexTerm", ...]
]
RecheckCacheOption = typing.Union[bool, typing.Literal["open"], float]
annotations = _Feature((3, 7, 0, "beta", 1), None, 16777216)
bfloat16 = dtype("bfloat16")
bool = dtype("bool")
byte = dtype("byte")
char = dtype("char")
complex128 = dtype("complex128")
complex64 = dtype("complex64")
float16 = dtype("float16")
float32 = dtype("float32")
float4_e2m1fn = dtype("float4_e2m1fn")
float64 = dtype("float64")
float8_e3m4 = dtype("float8_e3m4")
float8_e4m3b11fnuz = dtype("float8_e4m3b11fnuz")
float8_e4m3fn = dtype("float8_e4m3fn")
float8_e4m3fnuz = dtype("float8_e4m3fnuz")
float8_e5m2 = dtype("float8_e5m2")
float8_e5m2fnuz = dtype("float8_e5m2fnuz")
inf = numpy.inf
int16 = dtype("int16")
int2 = dtype("int2")
int32 = dtype("int32")
int4 = dtype("int4")
int64 = dtype("int64")
int8 = dtype("int8")
json = dtype("json")
newaxis = None
string = dtype("string")
uint16 = dtype("uint16")
uint32 = dtype("uint32")
uint64 = dtype("uint64")
uint8 = dtype("uint8")
ustring = dtype("ustring")
