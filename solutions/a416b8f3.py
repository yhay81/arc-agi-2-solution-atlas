"""Executable re-arc DSL program for ARC-AGI-2 task a416b8f3.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import Grid as ReArcGrid
from arc_agi_2_atlas.re_arc_dsl import hconcat
from arc_agi_2_atlas.types import Grid

TASK_ID = "a416b8f3"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = hconcat(grid, grid)
    return x0


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
