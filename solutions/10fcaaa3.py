"""Executable re-arc DSL program for ARC-AGI-2 task 10fcaaa3.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    asindices,
    difference,
    hconcat,
    ineighbors,
    mapply,
    mostcolor,
    ofcolor,
    underfill,
    vconcat,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "10fcaaa3"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = hconcat(grid, grid)
    x1 = vconcat(x0, x0)
    x2 = asindices(x1)
    x3 = mostcolor(grid)
    x4 = ofcolor(x1, x3)
    x5 = difference(x2, x4)
    x6 = mapply(ineighbors, x5)
    x7 = underfill(x1, EIGHT, x6)
    return x7


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
