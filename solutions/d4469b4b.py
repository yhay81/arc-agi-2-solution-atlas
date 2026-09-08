"""Executable re-arc DSL program for ARC-AGI-2 task d4469b4b.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FIVE,
    ONE,
    RIGHT,
    THREE_BY_THREE,
    TWO,
    TWO_BY_TWO,
    UNITY,
    ZERO,
    branch,
    canvas,
    combine,
    contained,
    fill,
    fork,
    hfrontier,
    palette,
    vfrontier,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d4469b4b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = palette(grid)
    x1 = contained(ONE, x0)
    x2 = contained(TWO, x0)
    x3 = branch(x1, UNITY, TWO_BY_TWO)
    x4 = branch(x2, RIGHT, x3)
    x5 = fork(combine, vfrontier, hfrontier)
    x6 = x5(x4)
    x7 = canvas(ZERO, THREE_BY_THREE)
    x8 = fill(x7, FIVE, x6)
    return x8


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
