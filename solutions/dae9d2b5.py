"""Executable re-arc DSL program for ARC-AGI-2 task dae9d2b5.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    SIX,
    TWO,
    TWO_BY_TWO,
    apply,
    branch,
    canvas,
    combine,
    equality,
    fill,
    first,
    hsplit,
    intersection,
    last,
    numcolors,
    ofcolor,
    other,
    palette,
    shape,
    vsplit,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "dae9d2b5"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = hsplit(grid, TWO)
    x1 = apply(numcolors, x0)
    x2 = equality(x1, TWO_BY_TWO)
    x3 = branch(x2, hsplit, vsplit)
    x4 = x3(grid, TWO)
    x5 = first(x4)
    x6 = last(x4)
    x7 = palette(x5)
    x8 = palette(x6)
    x9 = intersection(x7, x8)
    x10 = first(x9)
    x11 = palette(x5)
    x12 = other(x11, x10)
    x13 = palette(x6)
    x14 = other(x13, x10)
    x15 = shape(x5)
    x16 = canvas(x10, x15)
    x17 = ofcolor(x5, x12)
    x18 = ofcolor(x6, x14)
    x19 = combine(x17, x18)
    x20 = fill(x16, SIX, x19)
    return x20


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
