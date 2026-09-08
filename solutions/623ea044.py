"""Executable re-arc DSL program for ARC-AGI-2 task 623ea044.

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
    combine,
    fill,
    fork,
    leastcolor,
    mapply,
    ofcolor,
    rbind,
    shoot,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "623ea044"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = ofcolor(grid, x0)
    x2 = rbind(shoot, UNITY)
    x3 = rbind(shoot, NEG_UNITY)
    x4 = fork(combine, x2, x3)
    x5 = rbind(shoot, UP_RIGHT)
    x6 = rbind(shoot, DOWN_LEFT)
    x7 = fork(combine, x5, x6)
    x8 = fork(combine, x4, x7)
    x9 = mapply(x8, x1)
    x10 = fill(grid, x0, x9)
    return x10


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
