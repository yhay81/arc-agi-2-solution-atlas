"""Executable re-arc DSL program for ARC-AGI-2 task 150deff5.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    FIVE,
    FOUR,
    ONE,
    ORIGIN,
    THREE,
    THREE_BY_THREE,
    TWO,
    TWO_BY_TWO,
    UNITY,
    add,
    asobject,
    astuple,
    backdrop,
    canvas,
    chain,
    combine,
    compose,
    connect,
    difference,
    dneighbors,
    first,
    fork,
    identity,
    initset,
    insert,
    last,
    lbind,
    leastcolor,
    mapply,
    mostcolor,
    occurrences,
    ofcolor,
    outbox,
    paint,
    power,
    rbind,
    recolor,
    remove,
    rot90,
    shape,
    shift,
    trim,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "150deff5"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = leastcolor(grid)
    x2 = shape(grid)
    x3 = add(TWO, x2)
    x4 = canvas(x0, x3)
    x5 = asobject(grid)
    x6 = shift(x5, UNITY)
    x7 = paint(x4, x6)
    x8 = astuple(TWO, ONE)
    x9 = dneighbors(UNITY)
    x10 = remove(x8, x9)
    x11 = recolor(x0, x10)
    x12 = initset(UNITY)
    x13 = recolor(x1, x12)
    x14 = combine(x11, x13)
    x15 = astuple(THREE, ONE)
    x16 = connect(UNITY, x15)
    x17 = recolor(TWO, x16)
    x18 = initset(TWO_BY_TWO)
    x19 = insert(UNITY, x18)
    x20 = backdrop(x19)
    x21 = astuple(TWO, THREE)
    x22 = astuple(THREE, TWO)
    x23 = initset(x22)
    x24 = insert(x21, x23)
    x25 = insert(THREE_BY_THREE, x24)
    x26 = recolor(x1, x20)
    x27 = outbox(x20)
    x28 = difference(x27, x25)
    x29 = recolor(x0, x28)
    x30 = combine(x26, x29)
    x31 = recolor(EIGHT, x20)
    x32 = lbind(lbind, shift)
    x33 = compose(x32, last)
    x34 = lbind(fork, paint)
    x35 = lbind(x34, identity)
    x36 = lbind(lbind, mapply)
    x37 = compose(x36, x33)
    x38 = lbind(rbind, occurrences)
    x39 = compose(x38, first)
    x40 = fork(compose, x37, x39)
    x41 = compose(x35, x40)
    x42 = astuple(x14, x17)
    x43 = x41(x42)
    x44 = compose(rot90, x43)
    x45 = power(x44, FOUR)
    x46 = astuple(x30, x31)
    x47 = x41(x46)
    x48 = compose(rot90, x47)
    x49 = power(x48, FOUR)
    x50 = compose(x45, x49)
    x51 = initset(ORIGIN)
    x52 = difference(x51, x51)
    x53 = lbind(recolor, TWO)
    x54 = rbind(ofcolor, TWO)
    x55 = compose(x53, x54)
    x56 = lbind(recolor, EIGHT)
    x57 = rbind(ofcolor, EIGHT)
    x58 = compose(x56, x57)
    x59 = fork(combine, x55, x58)
    x60 = lbind(recolor, x0)
    x61 = compose(x60, x59)
    x62 = fork(paint, identity, x61)
    x63 = chain(x62, x50, first)
    x64 = chain(x59, x50, first)
    x65 = fork(combine, last, x64)
    x66 = fork(astuple, x63, x65)
    x67 = astuple(x7, x52)
    x68 = power(x66, FIVE)
    x69 = x68(x67)
    x70 = first(x69)
    x71 = last(x69)
    x72 = paint(x70, x71)
    x73 = trim(x72)
    return x73


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
