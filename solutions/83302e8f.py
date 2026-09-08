"""Executable re-arc DSL program for ARC-AGI-2 task 83302e8f.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    ORIGIN,
    THREE,
    F,
    T,
    both,
    chain,
    colorfilter,
    decrement,
    equality,
    fill,
    fork,
    height,
    index,
    merge,
    multiply,
    objects,
    ofcolor,
    positive,
    sfilter,
    size,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "83302e8f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = index(grid, ORIGIN)
    x1 = objects(grid, T, F, F)
    x2 = fork(multiply, height, width)
    x3 = fork(equality, size, x2)
    x4 = chain(positive, decrement, size)
    x5 = colorfilter(x1, x0)
    x6 = fork(both, x3, x4)
    x7 = sfilter(x5, x6)
    x8 = merge(x7)
    x9 = ofcolor(grid, x0)
    x10 = fill(grid, FOUR, x9)
    x11 = fill(x10, THREE, x8)
    return x11


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
