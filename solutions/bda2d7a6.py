"""Executable re-arc DSL program for ARC-AGI-2 task bda2d7a6.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    F,
    T,
    apply,
    branch,
    color,
    combine,
    compose,
    equality,
    first,
    last,
    maximum,
    mpapply,
    objects,
    order,
    paint,
    recolor,
    remove,
    repeat,
    shape,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "bda2d7a6"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = compose(maximum, shape)
    x2 = order(x0, x1)
    x3 = first(x2)
    x4 = last(x2)
    x5 = color(x3)
    x6 = color(x4)
    x7 = equality(x5, x6)
    x8 = combine(x3, x4)
    x9 = repeat(x8, ONE)
    x10 = remove(x3, x2)
    x11 = remove(x4, x10)
    x12 = combine(x9, x11)
    x13 = branch(x7, x12, x2)
    x14 = apply(color, x13)
    x15 = last(x13)
    x16 = remove(x15, x13)
    x17 = repeat(x15, ONE)
    x18 = combine(x17, x16)
    x19 = mpapply(recolor, x14, x18)
    x20 = paint(grid, x19)
    return x20


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
