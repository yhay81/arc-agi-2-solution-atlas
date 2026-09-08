"""Executable re-arc DSL program for ARC-AGI-2 task 31aa019c.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    canvas,
    fill,
    first,
    initset,
    leastcolor,
    mostcolor,
    neighbors,
    ofcolor,
    shape,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "31aa019c"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = ofcolor(grid, x0)
    x2 = first(x1)
    x3 = neighbors(x2)
    x4 = mostcolor(grid)
    x5 = shape(grid)
    x6 = canvas(x4, x5)
    x7 = initset(x2)
    x8 = fill(x6, x0, x7)
    x9 = fill(x8, TWO, x3)
    return x9


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
