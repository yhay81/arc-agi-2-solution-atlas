"""Executable re-arc DSL program for ARC-AGI-2 task dc433765.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    center,
    mostcolor,
    move,
    ofcolor,
    other,
    palette,
    recolor,
    remove,
    sign,
    subtract,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "dc433765"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = palette(grid)
    x2 = remove(x0, x1)
    x3 = other(x2, FOUR)
    x4 = ofcolor(grid, x3)
    x5 = ofcolor(grid, FOUR)
    x6 = center(x4)
    x7 = center(x5)
    x8 = subtract(x7, x6)
    x9 = sign(x8)
    x10 = recolor(x3, x4)
    x11 = move(grid, x10, x9)
    return x11


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
