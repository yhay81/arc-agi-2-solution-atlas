"""Executable re-arc DSL program for ARC-AGI-2 task 56ff96f3.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.re_arc_dsl import (
    backdrop,
    color,
    fgpartition,
    fork,
    mapply,
    paint,
    recolor,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "56ff96f3"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = fork(recolor, color, backdrop)
    x2 = mapply(x1, x0)
    x3 = paint(grid, x2)
    return x3


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
