"""Executable re-arc DSL program for ARC-AGI-2 task a1570a43.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.re_arc_dsl import (
    argmax,
    corners,
    difference,
    equality,
    fgpartition,
    fill,
    fork,
    height,
    increment,
    merge,
    mostcolor,
    multiply,
    normalize,
    paint,
    sfilter,
    shift,
    toindices,
    ulcorner,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "a1570a43"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = merge(x0)
    x2 = fork(equality, toindices, corners)
    x3 = fork(multiply, height, width)
    x4 = sfilter(x0, x2)
    x5 = argmax(x4, x3)
    x6 = difference(x1, x5)
    x7 = mostcolor(grid)
    x8 = fill(grid, x7, x6)
    x9 = normalize(x6)
    x10 = ulcorner(x5)
    x11 = increment(x10)
    x12 = shift(x9, x11)
    x13 = paint(x8, x12)
    return x13


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
