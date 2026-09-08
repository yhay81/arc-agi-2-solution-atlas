"""Executable re-arc DSL program for ARC-AGI-2 task 99b1bc43.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    THREE,
    TWO,
    branch,
    canvas,
    combine,
    difference,
    fill,
    first,
    frontiers,
    hsplit,
    intersection,
    last,
    ofcolor,
    palette,
    positive,
    sfilter,
    shape,
    size,
    vline,
    vsplit,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "99b1bc43"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = sfilter(x0, vline)
    x2 = size(x1)
    x3 = positive(x2)
    x4 = branch(x3, hsplit, vsplit)
    x5 = x4(grid, TWO)
    x6 = first(x5)
    x7 = last(x5)
    x8 = palette(x6)
    x9 = palette(x7)
    x10 = intersection(x8, x9)
    x11 = first(x10)
    x12 = shape(x6)
    x13 = canvas(x11, x12)
    x14 = ofcolor(x6, x11)
    x15 = ofcolor(x7, x11)
    x16 = combine(x14, x15)
    x17 = intersection(x14, x15)
    x18 = difference(x16, x17)
    x19 = fill(x13, THREE, x18)
    return x19


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
