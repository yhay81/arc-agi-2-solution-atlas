"""Executable re-arc DSL program for ARC-AGI-2 task 7447852a.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    ONE,
    ORIGIN,
    THREE,
    ZERO,
    F,
    T,
    canvas,
    centerofmass,
    chain,
    compose,
    divide,
    equality,
    fill,
    first,
    fork,
    hconcat,
    index,
    interval,
    last,
    mapply,
    multiply,
    objects,
    order,
    pair,
    rbind,
    sfilter,
    shape,
    size,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "7447852a"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = index(grid, ORIGIN)
    x1 = shape(grid)
    x2 = canvas(x0, x1)
    x3 = hconcat(grid, x2)
    x4 = objects(x3, F, F, T)
    x5 = compose(last, centerofmass)
    x6 = order(x4, x5)
    x7 = size(x6)
    x8 = interval(ZERO, x7, ONE)
    x9 = pair(x6, x8)
    x10 = rbind(multiply, THREE)
    x11 = rbind(divide, THREE)
    x12 = chain(x10, x11, last)
    x13 = fork(equality, last, x12)
    x14 = sfilter(x9, x13)
    x15 = mapply(first, x14)
    x16 = fill(grid, FOUR, x15)
    return x16


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
