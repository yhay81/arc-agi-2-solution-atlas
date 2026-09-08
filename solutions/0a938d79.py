"""Executable re-arc DSL program for ARC-AGI-2 task 0a938d79.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TEN,
    THREE,
    F,
    T,
    argmax,
    argmin,
    branch,
    color,
    combine,
    compose,
    dmirror,
    double,
    identity,
    interval,
    leftmost,
    mapply,
    multiply,
    objects,
    paint,
    portrait,
    recolor,
    subtract,
    tojvec,
    vfrontier,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "0a938d79"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = portrait(grid)
    x1 = branch(x0, dmirror, identity)
    x2 = x1(grid)
    x3 = objects(x2, T, F, T)
    x4 = argmin(x3, leftmost)
    x5 = argmax(x3, leftmost)
    x6 = color(x4)
    x7 = color(x5)
    x8 = leftmost(x4)
    x9 = leftmost(x5)
    x10 = subtract(x9, x8)
    x11 = double(x10)
    x12 = multiply(THREE, TEN)
    x13 = interval(x8, x12, x11)
    x14 = interval(x9, x12, x11)
    x15 = compose(vfrontier, tojvec)
    x16 = mapply(x15, x13)
    x17 = mapply(x15, x14)
    x18 = recolor(x6, x16)
    x19 = recolor(x7, x17)
    x20 = combine(x18, x19)
    x21 = paint(x2, x20)
    x22 = x1(x21)
    return x22


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
