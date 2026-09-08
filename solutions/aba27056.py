"""Executable re-arc DSL program for ARC-AGI-2 task aba27056.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    DOWN_LEFT,
    FOUR,
    LEFT,
    NEG_UNITY,
    RIGHT,
    UNITY,
    UP,
    UP_RIGHT,
    box,
    branch,
    combine,
    delta,
    equality,
    fgpartition,
    fill,
    intersection,
    leftmost,
    llcorner,
    lowermost,
    lrcorner,
    mapply,
    merge,
    rbind,
    rightmost,
    shoot,
    ulcorner,
    uppermost,
    urcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "aba27056"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = merge(x0)
    x2 = delta(x1)
    x3 = fill(grid, FOUR, x2)
    x4 = delta(x1)
    x5 = box(x1)
    x6 = intersection(x4, x5)
    x7 = uppermost(x6)
    x8 = uppermost(x1)
    x9 = equality(x7, x8)
    x10 = leftmost(x6)
    x11 = leftmost(x1)
    x12 = equality(x10, x11)
    x13 = lowermost(x6)
    x14 = lowermost(x1)
    x15 = equality(x13, x14)
    x16 = rightmost(x6)
    x17 = rightmost(x1)
    equality(x16, x17)
    x19 = urcorner(x6)
    x20 = ulcorner(x6)
    x21 = llcorner(x6)
    x22 = lrcorner(x6)
    x23 = branch(x15, x21, x22)
    x24 = branch(x12, x20, x23)
    x25 = branch(x9, x19, x24)
    x26 = branch(x15, x22, x19)
    x27 = branch(x12, x21, x26)
    x28 = branch(x9, x20, x27)
    x29 = branch(x15, DOWN_LEFT, UNITY)
    x30 = branch(x12, NEG_UNITY, x29)
    x31 = branch(x9, UP_RIGHT, x30)
    x32 = branch(x15, UNITY, UP_RIGHT)
    x33 = branch(x12, DOWN_LEFT, x32)
    x34 = branch(x9, NEG_UNITY, x33)
    x35 = branch(x15, DOWN, RIGHT)
    x36 = branch(x12, LEFT, x35)
    x37 = branch(x9, UP, x36)
    x38 = shoot(x25, x31)
    x39 = shoot(x28, x34)
    x40 = combine(x38, x39)
    x41 = rbind(shoot, x37)
    x42 = mapply(x41, x6)
    x43 = combine(x42, x40)
    x44 = fill(x3, FOUR, x43)
    return x44


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
