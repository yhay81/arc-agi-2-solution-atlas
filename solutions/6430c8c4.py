"""Executable re-arc DSL program for ARC-AGI-2 task 6430c8c4.

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
    fill,
    first,
    frontiers,
    hline,
    intersection,
    lefthalf,
    ofcolor,
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

TASK_ID = "6430c8c4"
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
    x8 = shape(x6)
    x9 = palette(x6)
    x10 = palette(x7)
    x11 = intersection(x9, x10)
    x12 = first(x11)
    x13 = ofcolor(x6, x12)
    x14 = ofcolor(x7, x12)
    x15 = intersection(x13, x14)
    x16 = canvas(x12, x8)
    x17 = fill(x16, THREE, x15)
    return x17


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
