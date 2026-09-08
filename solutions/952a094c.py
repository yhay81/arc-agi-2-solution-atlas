"""Executable re-arc DSL program for ARC-AGI-2 task 952a094c.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN_LEFT,
    NEG_UNITY,
    UNITY,
    UP_RIGHT,
    add,
    cover,
    fgpartition,
    fill,
    inbox,
    index,
    initset,
    llcorner,
    lrcorner,
    merge,
    ulcorner,
    urcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "952a094c"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = merge(x0)
    x2 = inbox(x1)
    x3 = cover(grid, x2)
    x4 = ulcorner(x2)
    x5 = index(grid, x4)
    x6 = lrcorner(x1)
    x7 = add(UNITY, x6)
    x8 = initset(x7)
    x9 = fill(x3, x5, x8)
    x10 = lrcorner(x2)
    x11 = index(grid, x10)
    x12 = ulcorner(x1)
    x13 = add(NEG_UNITY, x12)
    x14 = initset(x13)
    x15 = fill(x9, x11, x14)
    x16 = urcorner(x2)
    x17 = index(grid, x16)
    x18 = llcorner(x1)
    x19 = add(DOWN_LEFT, x18)
    x20 = initset(x19)
    x21 = fill(x15, x17, x20)
    x22 = llcorner(x2)
    x23 = index(grid, x22)
    x24 = urcorner(x1)
    x25 = add(UP_RIGHT, x24)
    x26 = initset(x25)
    x27 = fill(x21, x23, x26)
    return x27


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
