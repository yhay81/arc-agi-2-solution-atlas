"""Executable re-arc DSL program for ARC-AGI-2 task e48d4e1a.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.re_arc_dsl import (
    add,
    argmax,
    asobject,
    astuple,
    color,
    colorcount,
    combine,
    difference,
    fill,
    frontiers,
    height,
    hfrontier,
    initset,
    leastcolor,
    leftmost,
    merge,
    mostcolor,
    multiply,
    ofcolor,
    position,
    toindices,
    uppermost,
    vfrontier,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "e48d4e1a"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = merge(x0)
    x2 = color(x1)
    x3 = asobject(grid)
    x4 = difference(x3, x1)
    x5 = leastcolor(x4)
    x6 = colorcount(grid, x5)
    x7 = mostcolor(x4)
    x8 = ofcolor(grid, x5)
    x9 = toindices(x1)
    x10 = combine(x9, x8)
    x11 = fill(grid, x7, x10)
    x12 = argmax(x0, width)
    x13 = uppermost(x12)
    x14 = argmax(x0, height)
    x15 = leftmost(x14)
    x16 = astuple(x13, x15)
    x17 = initset(x16)
    x18 = position(x8, x17)
    x19 = multiply(x18, x6)
    x20 = add(x16, x19)
    x21 = hfrontier(x20)
    x22 = vfrontier(x20)
    x23 = combine(x21, x22)
    x24 = fill(x11, x2, x23)
    return x24


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
