"""Executable re-arc DSL program for ARC-AGI-2 task ec883f72.

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
    argmax,
    color,
    combine,
    fill,
    fork,
    height,
    llcorner,
    lrcorner,
    multiply,
    other,
    palette,
    partition,
    remove,
    shoot,
    ulcorner,
    urcorner,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "ec883f72"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fork(multiply, height, width)
    x1 = partition(grid)
    x2 = argmax(x1, x0)
    x3 = remove(x2, x1)
    x4 = argmax(x3, x0)
    x5 = other(x3, x4)
    palette(grid)
    x7 = lrcorner(x4)
    x8 = add(x7, UNITY)
    x9 = llcorner(x4)
    x10 = add(x9, DOWN_LEFT)
    x11 = urcorner(x4)
    x12 = add(x11, UP_RIGHT)
    x13 = ulcorner(x4)
    x14 = add(x13, NEG_UNITY)
    x15 = shoot(x8, UNITY)
    x16 = shoot(x10, DOWN_LEFT)
    x17 = shoot(x12, UP_RIGHT)
    x18 = shoot(x14, NEG_UNITY)
    x19 = combine(x15, x16)
    x20 = combine(x17, x18)
    x21 = combine(x19, x20)
    x22 = color(x5)
    x23 = fill(grid, x22, x21)
    return x23


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
