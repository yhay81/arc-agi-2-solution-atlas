"""Executable re-arc DSL program for ARC-AGI-2 task 23581191.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    combine,
    compose,
    fill,
    first,
    fork,
    hfrontier,
    intersection,
    last,
    lbind,
    mapply,
    mostcolor,
    ofcolor,
    palette,
    remove,
    totuple,
    vfrontier,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "23581191"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = palette(grid)
    x2 = remove(x0, x1)
    x3 = totuple(x2)
    x4 = fork(combine, hfrontier, vfrontier)
    x5 = lbind(mapply, x4)
    x6 = lbind(ofcolor, grid)
    x7 = compose(x5, x6)
    x8 = first(x3)
    x9 = last(x3)
    x10 = x7(x8)
    x11 = x7(x9)
    x12 = ofcolor(grid, x0)
    x13 = intersection(x12, x10)
    x14 = intersection(x12, x11)
    x15 = intersection(x10, x11)
    x16 = intersection(x12, x15)
    x17 = fill(grid, x8, x13)
    x18 = fill(x17, x9, x14)
    x19 = fill(x18, TWO, x16)
    return x19


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
