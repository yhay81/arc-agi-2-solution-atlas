"""Executable re-arc DSL program for ARC-AGI-2 task d4a91cb9.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    FOUR,
    TWO,
    astuple,
    combine,
    connect,
    first,
    last,
    ofcolor,
    underfill,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d4a91cb9"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = ofcolor(grid, EIGHT)
    x1 = ofcolor(grid, TWO)
    x2 = first(x0)
    x3 = first(x1)
    x4 = last(x2)
    x5 = first(x3)
    x6 = astuple(x5, x4)
    x7 = connect(x6, x2)
    x8 = connect(x6, x3)
    x9 = combine(x7, x8)
    x10 = underfill(grid, FOUR, x9)
    return x10


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
