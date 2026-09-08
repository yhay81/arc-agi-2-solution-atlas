"""Executable re-arc DSL program for ARC-AGI-2 task 2204b7a8.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ORIGIN,
    astuple,
    bottomhalf,
    branch,
    canvas,
    decrement,
    dedupe,
    dmirror,
    equality,
    even,
    first,
    flip,
    hconcat,
    height,
    identity,
    index,
    lefthalf,
    mostcolor,
    palette,
    remove,
    replace,
    righthalf,
    shape,
    size,
    tophalf,
    vconcat,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "2204b7a8"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = first(grid)
    x1 = dedupe(x0)
    x2 = size(x1)
    x3 = equality(x2, ONE)
    x4 = flip(x3)
    x5 = branch(x4, lefthalf, tophalf)
    x6 = branch(x4, righthalf, bottomhalf)
    x7 = branch(x4, hconcat, vconcat)
    x8 = x5(grid)
    x9 = x6(grid)
    x10 = index(x8, ORIGIN)
    x11 = shape(x9)
    x12 = decrement(x11)
    x13 = index(x9, x12)
    x14 = mostcolor(grid)
    x15 = mostcolor(grid)
    x16 = palette(grid)
    x17 = remove(x10, x16)
    x18 = remove(x13, x17)
    x19 = remove(x15, x18)
    x20 = first(x19)
    x21 = replace(x8, x20, x10)
    x22 = branch(x4, dmirror, identity)
    x23 = branch(x4, height, width)
    x24 = x23(grid)
    x25 = astuple(ONE, x24)
    x26 = canvas(x14, x25)
    x27 = x22(x26)
    x28 = replace(x9, x20, x13)
    x29 = x7(x21, x27)
    x30 = branch(x4, width, height)
    x31 = x30(grid)
    x32 = even(x31)
    x33 = branch(x32, x21, x29)
    x34 = x7(x33, x28)
    return x34


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
