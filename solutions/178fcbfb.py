"""Executable re-arc DSL program for ARC-AGI-2 task 178fcbfb.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    THREE,
    TWO,
    fill,
    hfrontier,
    mapply,
    ofcolor,
    vfrontier,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "178fcbfb"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = ofcolor(grid, TWO)
    x1 = ofcolor(grid, THREE)
    x2 = ofcolor(grid, ONE)
    x3 = mapply(vfrontier, x0)
    x4 = mapply(hfrontier, x1)
    x5 = mapply(hfrontier, x2)
    x6 = fill(grid, TWO, x3)
    x7 = fill(x6, THREE, x4)
    x8 = fill(x7, ONE, x5)
    return x8


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
