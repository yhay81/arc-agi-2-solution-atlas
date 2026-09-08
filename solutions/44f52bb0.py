"""Executable re-arc DSL program for ARC-AGI-2 task 44f52bb0.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    SEVEN,
    UNITY,
    branch,
    canvas,
    either,
    equality,
    hmirror,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "44f52bb0"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = vmirror(grid)
    x1 = equality(x0, grid)
    x2 = hmirror(grid)
    x3 = equality(x2, grid)
    x4 = either(x1, x3)
    x5 = branch(x4, ONE, SEVEN)
    x6 = canvas(x5, UNITY)
    return x6


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
