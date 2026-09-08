"""Executable re-arc DSL program for ARC-AGI-2 task e509e548.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    SIX,
    TWO,
    ZERO,
    F,
    T,
    add,
    box,
    compose,
    decrement,
    difference,
    equality,
    fill,
    fork,
    height,
    matcher,
    merge,
    objects,
    sfilter,
    size,
    toindices,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "e509e548"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = fork(add, height, width)
    x2 = compose(decrement, x1)
    x3 = fork(equality, size, x2)
    x4 = fork(difference, toindices, box)
    x5 = compose(size, x4)
    x6 = matcher(x5, ZERO)
    x7 = sfilter(x0, x3)
    x8 = difference(x0, x7)
    x9 = sfilter(x8, x6)
    x10 = merge(x0)
    x11 = fill(grid, TWO, x10)
    x12 = merge(x7)
    x13 = fill(x11, ONE, x12)
    x14 = merge(x9)
    x15 = fill(x13, SIX, x14)
    return x15


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
