"""Executable re-arc DSL program for ARC-AGI-2 task 67a423a3.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    backdrop,
    fill,
    first,
    intersection,
    last,
    mostcolor,
    ofcolor,
    outbox,
    palette,
    remove,
    totuple,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "67a423a3"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = palette(grid)
    x2 = remove(x0, x1)
    x3 = totuple(x2)
    x4 = first(x3)
    x5 = last(x3)
    x6 = ofcolor(grid, x4)
    x7 = backdrop(x6)
    x8 = ofcolor(grid, x5)
    x9 = backdrop(x8)
    x10 = intersection(x7, x9)
    x11 = outbox(x10)
    x12 = fill(grid, FOUR, x11)
    return x12


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
