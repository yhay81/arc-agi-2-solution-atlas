"""Executable re-arc DSL program for ARC-AGI-2 task ce4f8723.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    THREE,
    bottomhalf,
    branch,
    canvas,
    combine,
    fill,
    first,
    frontiers,
    hline,
    intersection,
    lefthalf,
    ofcolor,
    other,
    palette,
    positive,
    righthalf,
    sfilter,
    shape,
    size,
    tophalf,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "ce4f8723"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = sfilter(x0, hline)
    x2 = size(x1)
    x3 = positive(x2)
    x4 = branch(x3, tophalf, lefthalf)
    x5 = branch(x3, bottomhalf, righthalf)
    x6 = x4(grid)
    x7 = x5(grid)
    x8 = palette(x6)
    x9 = palette(x7)
    x10 = intersection(x8, x9)
    x11 = first(x10)
    x12 = shape(x6)
    x13 = canvas(x11, x12)
    x14 = palette(x6)
    x15 = other(x14, x11)
    x16 = palette(x7)
    x17 = other(x16, x11)
    x18 = ofcolor(x6, x15)
    x19 = ofcolor(x7, x17)
    x20 = combine(x18, x19)
    x21 = fill(x13, THREE, x20)
    return x21


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
