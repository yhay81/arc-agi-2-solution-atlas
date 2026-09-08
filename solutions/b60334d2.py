"""Executable re-arc DSL program for ARC-AGI-2 task b60334d2.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    dneighbors,
    fill,
    ineighbors,
    leastcolor,
    mapply,
    mostcolor,
    ofcolor,
    replace,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "b60334d2"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = mostcolor(grid)
    x2 = ofcolor(grid, x0)
    x3 = replace(grid, x0, x1)
    x4 = mapply(dneighbors, x2)
    x5 = mapply(ineighbors, x2)
    x6 = fill(x3, ONE, x4)
    x7 = fill(x6, x0, x5)
    return x7


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
