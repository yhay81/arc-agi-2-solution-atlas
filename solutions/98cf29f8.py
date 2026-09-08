"""Executable re-arc DSL program for ARC-AGI-2 task 98cf29f8.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ORIGIN,
    RIGHT,
    TWO,
    UNITY,
    ZERO_BY_TWO,
    add,
    apply,
    asindices,
    asobject,
    astuple,
    backdrop,
    box,
    canvas,
    color,
    combine,
    dmirror,
    equality,
    extract,
    fill,
    fork,
    gravitate,
    identity,
    initset,
    insert,
    lbind,
    mapply,
    mostcolor,
    occurrences,
    ofcolor,
    other,
    paint,
    palette,
    recolor,
    remove,
    replace,
    shape,
    shift,
    toindices,
    toobject,
    trim,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "98cf29f8"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asindices(grid)
    x1 = box(x0)
    x2 = toobject(x1, grid)
    x3 = mostcolor(x2)
    x4 = shape(grid)
    x5 = add(TWO, x4)
    x6 = canvas(x3, x5)
    x7 = asobject(grid)
    x8 = shift(x7, UNITY)
    x9 = paint(x6, x8)
    x10 = palette(x9)
    x11 = remove(x3, x10)
    x12 = lbind(ofcolor, x9)
    x13 = fork(recolor, identity, x12)
    x14 = apply(x13, x11)
    x15 = fork(equality, toindices, backdrop)
    x16 = extract(x14, x15)
    x17 = other(x14, x16)
    x18 = color(x17)
    x19 = astuple(x18, RIGHT)
    x20 = initset(ZERO_BY_TWO)
    x21 = insert(ORIGIN, x20)
    x22 = recolor(x3, x21)
    x23 = insert(x19, x22)
    x24 = dmirror(x23)
    x25 = lbind(shift, x23)
    x26 = occurrences(x9, x23)
    x27 = mapply(x25, x26)
    x28 = lbind(shift, x24)
    x29 = occurrences(x9, x24)
    x30 = mapply(x28, x29)
    x31 = combine(x27, x30)
    x32 = fill(x9, x3, x31)
    x33 = ofcolor(x32, x18)
    x34 = gravitate(x33, x16)
    x35 = replace(x9, x18, x3)
    x36 = shift(x33, x34)
    x37 = fill(x35, x18, x36)
    x38 = trim(x37)
    return x38


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
