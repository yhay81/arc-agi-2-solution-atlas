"""Executable re-arc DSL program for ARC-AGI-2 task 7b7f7511.

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
    branch,
    equality,
    lefthalf,
    righthalf,
    tophalf,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "7b7f7511"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = lefthalf(grid)
    x1 = righthalf(grid)
    x2 = equality(x0, x1)
    x3 = branch(x2, lefthalf, tophalf)
    x4 = x3(grid)
    return x4


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
