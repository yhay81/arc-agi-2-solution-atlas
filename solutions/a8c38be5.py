"""Executable re-arc DSL program for ARC-AGI-2 task a8c38be5.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    TWO,
    ZERO,
    F,
    T,
    add,
    argmax,
    astuple,
    both,
    canvas,
    chain,
    color,
    colorcount,
    combine,
    compose,
    connect,
    contained,
    difference,
    equality,
    first,
    flip,
    fork,
    height,
    increment,
    index,
    last,
    lbind,
    leftmost,
    llcorner,
    lowermost,
    lrcorner,
    matcher,
    mostcolor,
    normalize,
    objects,
    paint,
    palette,
    rbind,
    remove,
    rightmost,
    sfilter,
    shift,
    size,
    subtract,
    toindices,
    toivec,
    tojvec,
    ulcorner,
    uppermost,
    urcorner,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "a8c38be5"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = mostcolor(grid)
    x2 = palette(grid)
    x3 = remove(x1, x2)
    x4 = lbind(colorcount, grid)
    x5 = argmax(x3, x4)
    x6 = astuple(x1, x5)
    x7 = rbind(contained, x6)
    x8 = chain(flip, x7, color)
    x9 = sfilter(x0, x8)
    x10 = fork(connect, ulcorner, urcorner)
    x11 = fork(connect, ulcorner, llcorner)
    x12 = fork(combine, x10, x11)
    x13 = fork(equality, toindices, x12)
    x14 = fork(connect, urcorner, ulcorner)
    x15 = fork(connect, urcorner, lrcorner)
    x16 = fork(combine, x14, x15)
    x17 = fork(equality, toindices, x16)
    x18 = fork(connect, llcorner, ulcorner)
    x19 = fork(connect, llcorner, lrcorner)
    x20 = fork(combine, x18, x19)
    x21 = fork(equality, toindices, x20)
    x22 = fork(connect, lrcorner, llcorner)
    x23 = fork(connect, lrcorner, urcorner)
    x24 = fork(combine, x22, x23)
    x25 = fork(equality, toindices, x24)
    x26 = fork(contained, lrcorner, toindices)
    x27 = compose(flip, x26)
    x28 = fork(contained, llcorner, toindices)
    x29 = compose(flip, x28)
    x30 = fork(contained, urcorner, toindices)
    x31 = compose(flip, x30)
    x32 = fork(contained, ulcorner, toindices)
    x33 = compose(flip, x32)
    x34 = fork(both, x27, x29)
    x35 = fork(both, x31, x33)
    x36 = fork(both, x31, x27)
    x37 = fork(both, x33, x29)
    x38 = lbind(matcher, first)
    x39 = compose(x38, lowermost)
    x40 = fork(sfilter, toindices, x39)
    x41 = compose(size, x40)
    x42 = matcher(x41, ONE)
    x43 = lbind(matcher, first)
    x44 = compose(x43, uppermost)
    x45 = fork(sfilter, toindices, x44)
    x46 = compose(size, x45)
    x47 = matcher(x46, ONE)
    x48 = lbind(matcher, last)
    x49 = compose(x48, rightmost)
    x50 = fork(sfilter, toindices, x49)
    x51 = compose(size, x50)
    x52 = matcher(x51, ONE)
    x53 = lbind(matcher, last)
    x54 = compose(x53, leftmost)
    x55 = fork(sfilter, toindices, x54)
    x56 = compose(size, x55)
    x57 = matcher(x56, ONE)
    x58 = fork(both, x34, x42)
    x59 = fork(both, x35, x47)
    x60 = fork(both, x36, x52)
    x61 = fork(both, x37, x57)
    x62 = fork(connect, ulcorner, urcorner)
    x63 = fork(difference, x62, toindices)
    x64 = compose(size, x63)
    x65 = matcher(x64, ZERO)
    x66 = fork(connect, llcorner, lrcorner)
    x67 = fork(difference, x66, toindices)
    x68 = compose(size, x67)
    x69 = matcher(x68, ZERO)
    x70 = fork(connect, ulcorner, llcorner)
    x71 = fork(difference, x70, toindices)
    x72 = compose(size, x71)
    x73 = matcher(x72, ZERO)
    x74 = fork(connect, urcorner, lrcorner)
    x75 = fork(difference, x74, toindices)
    x76 = compose(size, x75)
    x77 = matcher(x76, ZERO)
    x78 = fork(both, x65, x58)
    x79 = fork(both, x69, x59)
    x80 = fork(both, x73, x60)
    x81 = fork(both, x77, x61)
    x82 = argmax(x9, x13)
    x83 = argmax(x9, x17)
    x84 = argmax(x9, x21)
    x85 = argmax(x9, x25)
    x86 = argmax(x9, x78)
    x87 = argmax(x9, x79)
    x88 = argmax(x9, x80)
    x89 = argmax(x9, x81)
    x90 = height(x82)
    x91 = height(x84)
    x92 = add(x90, x91)
    x93 = height(x88)
    x94 = add(x93, TWO)
    x95 = add(x92, x94)
    x96 = width(x82)
    x97 = width(x83)
    x98 = add(x96, x97)
    x99 = width(x86)
    x100 = add(x99, TWO)
    x101 = add(x98, x100)
    x102 = ulcorner(x82)
    x103 = increment(x102)
    x104 = index(grid, x103)
    x105 = astuple(x95, x101)
    x106 = canvas(x104, x105)
    x107 = normalize(x82)
    x108 = paint(x106, x107)
    x109 = normalize(x83)
    x110 = width(x83)
    x111 = subtract(x101, x110)
    x112 = tojvec(x111)
    x113 = shift(x109, x112)
    x114 = paint(x108, x113)
    x115 = normalize(x84)
    x116 = height(x84)
    x117 = subtract(x95, x116)
    x118 = toivec(x117)
    x119 = shift(x115, x118)
    x120 = paint(x114, x119)
    x121 = normalize(x85)
    x122 = height(x85)
    x123 = subtract(x95, x122)
    x124 = width(x85)
    x125 = subtract(x101, x124)
    x126 = astuple(x123, x125)
    x127 = shift(x121, x126)
    x128 = paint(x120, x127)
    x129 = normalize(x88)
    x130 = height(x82)
    x131 = increment(x130)
    x132 = toivec(x131)
    x133 = shift(x129, x132)
    x134 = paint(x128, x133)
    x135 = normalize(x86)
    x136 = width(x82)
    x137 = increment(x136)
    x138 = tojvec(x137)
    x139 = shift(x135, x138)
    x140 = paint(x134, x139)
    x141 = normalize(x89)
    x142 = height(x83)
    x143 = increment(x142)
    x144 = width(x89)
    x145 = subtract(x101, x144)
    x146 = astuple(x143, x145)
    x147 = shift(x141, x146)
    x148 = paint(x140, x147)
    x149 = normalize(x87)
    x150 = height(x87)
    x151 = subtract(x95, x150)
    x152 = width(x84)
    x153 = increment(x152)
    x154 = astuple(x151, x153)
    x155 = shift(x149, x154)
    x156 = paint(x148, x155)
    return x156


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
