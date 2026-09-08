"""Executable re-arc DSL program for ARC-AGI-2 task 28bf18c6.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import Grid as ReArcGrid
from arc_agi_2_atlas.re_arc_dsl import T, first, hconcat, objects, subgrid
from arc_agi_2_atlas.types import Grid

TASK_ID = "28bf18c6"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, T, T)
    x1 = first(x0)
    x2 = subgrid(x1, grid)
    x3 = hconcat(x2, x2)
    return x3


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
