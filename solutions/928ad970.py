"""Executable re-arc DSL program for ARC-AGI-2 task 928ad970.

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
    fill,
    inbox,
    leastcolor,
    mostcolor,
    ofcolor,
    other,
    palette,
    remove,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "928ad970"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = ofcolor(grid, x0)
    x2 = leastcolor(grid)
    x3 = palette(grid)
    x4 = remove(x2, x3)
    x5 = mostcolor(grid)
    x6 = other(x4, x5)
    x7 = inbox(x1)
    x8 = fill(grid, x6, x7)
    return x8


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
