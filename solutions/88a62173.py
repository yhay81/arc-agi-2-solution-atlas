"""Executable re-arc DSL program for ARC-AGI-2 task 88a62173.

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
    astuple,
    bottomhalf,
    combine,
    leastcommon,
    lefthalf,
    righthalf,
    tophalf,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "88a62173"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = lefthalf(grid)
    x1 = righthalf(grid)
    x2 = tophalf(x0)
    x3 = tophalf(x1)
    x4 = bottomhalf(x0)
    x5 = bottomhalf(x1)
    x6 = astuple(x2, x3)
    x7 = astuple(x4, x5)
    x8 = combine(x6, x7)
    x9 = leastcommon(x8)
    return x9


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
