"""Executable re-arc DSL program for ARC-AGI-2 task e40b9e2f.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NEG_ONE,
    ONE,
    ORIGIN,
    SEVEN,
    add,
    argmin,
    asobject,
    astuple,
    backdrop,
    both,
    branch,
    center,
    chain,
    colorcount,
    combine,
    compose,
    decrement,
    difference,
    equality,
    fgpartition,
    first,
    fork,
    greater,
    halve,
    height,
    identity,
    increment,
    initset,
    insert,
    interval,
    invert,
    last,
    lbind,
    leftmost,
    manhattan,
    mapply,
    matcher,
    merge,
    mostcolor,
    multiply,
    occurrences,
    paint,
    product,
    rbind,
    repeat,
    rot90,
    rot180,
    rot270,
    sfilter,
    shape,
    shift,
    subgrid,
    subtract,
    uppermost,
    valmax,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "e40b9e2f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = merge(x0)
    x2 = mostcolor(grid)
    x3 = uppermost(x1)
    x4 = leftmost(x1)
    x5 = height(x1)
    x6 = width(x1)
    x7 = interval(SEVEN, ONE, NEG_ONE)
    x8 = add(x3, x5)
    x9 = increment(x8)
    x10 = lbind(subtract, x9)
    x11 = add(x4, x6)
    x12 = increment(x11)
    x13 = lbind(subtract, x12)
    x14 = lbind(interval, x3)
    x15 = rbind(x14, ONE)
    x16 = compose(x15, x10)
    x17 = lbind(interval, x4)
    x18 = rbind(x17, ONE)
    x19 = compose(x18, x13)
    x20 = fork(product, x16, x19)
    x21 = fork(equality, identity, rot90)
    x22 = fork(equality, identity, rot180)
    x23 = fork(equality, identity, rot270)
    x24 = fork(both, x22, x23)
    x25 = fork(both, x21, x24)
    x26 = fork(astuple, identity, identity)
    x27 = fork(multiply, identity, identity)
    x28 = compose(decrement, x27)
    x29 = initset(ORIGIN)
    x30 = difference(x29, x29)
    x31 = rbind(branch, x30)
    x32 = rbind(colorcount, x2)
    x33 = rbind(subgrid, grid)
    x34 = lbind(compose, backdrop)
    x35 = lbind(fork, insert)
    x36 = lbind(x35, identity)
    x37 = lbind(compose, initset)
    x38 = chain(x34, x36, x37)
    x39 = lbind(rbind, add)
    x40 = chain(x38, x39, decrement)
    x41 = lbind(fork, x31)
    x42 = lbind(fork, both)
    x43 = lbind(x42, x25)
    x44 = rbind(compose, shape)
    x45 = compose(x43, x44)
    x46 = rbind(compose, x32)
    x47 = lbind(lbind, greater)
    x48 = chain(x46, x47, x28)
    x49 = lbind(rbind, equality)
    x50 = chain(x45, x49, x26)
    x51 = fork(x42, x48, x50)
    x52 = lbind(compose, x33)
    x53 = compose(x52, x40)
    x54 = fork(compose, x51, x53)
    x55 = lbind(compose, initset)
    x56 = lbind(rbind, astuple)
    x57 = compose(x55, x56)
    x58 = fork(x41, x54, x57)
    x59 = fork(mapply, x58, x20)
    x60 = center(x1)
    x61 = astuple(x60, ONE)
    x62 = repeat(x61, ONE)
    x63 = mapply(x59, x7)
    x64 = combine(x62, x63)
    x65 = valmax(x64, last)
    x66 = matcher(last, x65)
    x67 = sfilter(x64, x66)
    x68 = center(x1)
    x69 = initset(x68)
    x70 = rbind(manhattan, x69)
    x71 = compose(halve, last)
    x72 = fork(add, first, x71)
    x73 = compose(initset, x72)
    x74 = compose(x70, x73)
    x75 = argmin(x67, x74)
    x76 = first(x75)
    x77 = last(x75)
    x78 = decrement(x77)
    x79 = add(x76, x78)
    x80 = initset(x79)
    x81 = insert(x76, x80)
    x82 = backdrop(x81)
    x83 = subgrid(x82, grid)
    x84 = asobject(x83)
    x85 = rot90(grid)
    x86 = fgpartition(x85)
    x87 = merge(x86)
    x88 = rot180(grid)
    x89 = fgpartition(x88)
    x90 = merge(x89)
    x91 = rot270(grid)
    x92 = fgpartition(x91)
    x93 = merge(x92)
    x94 = rot90(grid)
    x95 = occurrences(x94, x84)
    x96 = first(x95)
    x97 = invert(x96)
    x98 = shift(x87, x97)
    x99 = shift(x98, x76)
    x100 = rot180(grid)
    x101 = occurrences(x100, x84)
    x102 = first(x101)
    x103 = invert(x102)
    x104 = shift(x90, x103)
    x105 = shift(x104, x76)
    x106 = rot270(grid)
    x107 = occurrences(x106, x84)
    x108 = first(x107)
    x109 = invert(x108)
    x110 = shift(x93, x109)
    x111 = shift(x110, x76)
    x112 = combine(x99, x105)
    x113 = combine(x112, x111)
    x114 = paint(grid, x113)
    return x114


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
