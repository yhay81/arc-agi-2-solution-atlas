"""Executable re-arc DSL program for ARC-AGI-2 task ea786f4a.

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
    halve,
    index,
    rbind,
    shape,
    shoot,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "ea786f4a"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = shape(grid)
    x1 = halve(x0)
    x2 = rbind(shoot, UP_RIGHT)
    x3 = rbind(shoot, DOWN_LEFT)
    x4 = fork(combine, x2, x3)
    x5 = rbind(shoot, UNITY)
    x6 = rbind(shoot, NEG_UNITY)
    x7 = fork(combine, x5, x6)
    x8 = fork(combine, x4, x7)
    x9 = index(grid, x1)
    x10 = x8(x1)
    x11 = fill(grid, x9, x10)
    return x11


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
