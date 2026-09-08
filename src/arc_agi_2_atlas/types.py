"""Shared types and validation for ARC grids."""

from collections.abc import Sequence

type Cell = int
type Grid = list[list[Cell]]
type ReadonlyGrid = Sequence[Sequence[Cell]]


def normalize_grid(value: object) -> Grid:
    """Return a validated mutable ARC grid."""
    if not isinstance(value, list) or not value:
        raise ValueError("grid must be a non-empty list of rows")
    if not all(isinstance(row, list) and row for row in value):
        raise ValueError("every grid row must be a non-empty list")

    width = len(value[0])
    result: Grid = []
    for row in value:
        if len(row) != width:
            raise ValueError("grid must be rectangular")
        if not all(type(cell) is int and 0 <= cell <= 9 for cell in row):
            raise ValueError("ARC cells must be integers from 0 through 9")
        result.append(list(row))
    return result
