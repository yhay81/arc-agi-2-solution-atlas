"""Executable re-arc DSL program for ARC-AGI-2 task fafffa47.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    both,
    bottomhalf,
    branch,
    canvas,
    equality,
    fill,
    first,
    flip,
    hsplit,
    intersection,
    last,
    lefthalf,
    numcolors,
    ofcolor,
    palette,
    righthalf,
    shape,
    tophalf,
    vsplit,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "fafffa47"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = tophalf(grid)
    x1 = numcolors(x0)
    x2 = equality(x1, TWO)
    x3 = bottomhalf(grid)
    x4 = numcolors(x3)
    x5 = equality(x4, TWO)
    x6 = both(x2, x5)
    x7 = lefthalf(grid)
    x8 = numcolors(x7)
    x9 = equality(x8, TWO)
    x10 = righthalf(grid)
    x11 = numcolors(x10)
    x12 = equality(x11, TWO)
    x13 = both(x9, x12)
    x14 = flip(x13)
    x15 = both(x6, x14)
    x16 = branch(x15, vsplit, hsplit)
    x17 = x16(grid, TWO)
    x18 = first(x17)
    x19 = last(x17)
    x20 = palette(x18)
    x21 = palette(x19)
    x22 = intersection(x20, x21)
    x23 = first(x22)
    x24 = shape(x18)
    x25 = canvas(x23, x24)
    x26 = ofcolor(x18, x23)
    x27 = ofcolor(x19, x23)
    x28 = intersection(x26, x27)
    x29 = fill(x25, TWO, x28)
    return x29


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
