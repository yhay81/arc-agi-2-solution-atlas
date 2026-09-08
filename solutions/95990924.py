"""Executable re-arc DSL program for ARC-AGI-2 task 95990924.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN_LEFT,
    FOUR,
    NEG_UNITY,
    ONE,
    THREE,
    TWO,
    UNITY,
    UP_RIGHT,
    F,
    T,
    apply,
    fill,
    llcorner,
    lrcorner,
    objects,
    shift,
    ulcorner,
    urcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "95990924"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = apply(ulcorner, x0)
    x2 = apply(urcorner, x0)
    x3 = apply(llcorner, x0)
    x4 = apply(lrcorner, x0)
    x5 = shift(x1, NEG_UNITY)
    x6 = shift(x2, UP_RIGHT)
    x7 = shift(x3, DOWN_LEFT)
    x8 = shift(x4, UNITY)
    x9 = fill(grid, ONE, x5)
    x10 = fill(x9, TWO, x6)
    x11 = fill(x10, THREE, x7)
    x12 = fill(x11, FOUR, x8)
    return x12


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
