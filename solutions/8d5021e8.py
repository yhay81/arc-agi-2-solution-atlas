"""Executable re-arc DSL program for ARC-AGI-2 task 8d5021e8.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import Grid as ReArcGrid
from arc_agi_2_atlas.re_arc_dsl import hconcat, hmirror, vconcat, vmirror
from arc_agi_2_atlas.types import Grid

TASK_ID = "8d5021e8"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = vmirror(grid)
    x1 = hconcat(x0, grid)
    x2 = hmirror(x1)
    x3 = vconcat(x1, x2)
    x4 = vconcat(x3, x1)
    x5 = hmirror(x4)
    return x5


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
