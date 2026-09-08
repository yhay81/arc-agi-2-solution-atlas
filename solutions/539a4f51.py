"""Executable re-arc DSL program for ARC-AGI-2 task 539a4f51.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ORIGIN,
    TWO,
    ZERO,
    F,
    T,
    argmin,
    asobject,
    astuple,
    chain,
    cmirror,
    combine,
    compose,
    contained,
    divide,
    dmirror,
    double,
    extract,
    first,
    flip,
    fork,
    greater,
    height,
    hmirror,
    identity,
    increment,
    initset,
    last,
    lbind,
    matcher,
    merge,
    multiply,
    objects,
    paint,
    rapply,
    rbind,
    repeat,
    sfilter,
    size,
    toindices,
    upscale,
    vmirror,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "539a4f51"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = astuple(identity, cmirror)
    x1 = astuple(hmirror, vmirror)
    x2 = combine(x0, x1)
    x3 = fork(multiply, height, width)
    x4 = rbind(objects, F)
    x5 = rbind(x4, F)
    x6 = rbind(x5, T)
    x7 = rbind(argmin, x3)
    x8 = lbind(contained, ORIGIN)
    x9 = chain(x8, toindices, x7)
    x10 = compose(x9, x6)
    x11 = lbind(compose, x10)
    x12 = rbind(rapply, grid)
    x13 = compose(initset, x11)
    x14 = chain(first, x12, x13)
    x15 = extract(x2, x14)
    x16 = x15(grid)
    x17 = height(grid)
    x18 = first(x16)
    x19 = matcher(identity, ZERO)
    x20 = compose(flip, x19)
    x21 = sfilter(x18, x20)
    x22 = size(x21)
    x23 = divide(x17, x22)
    x24 = increment(x23)
    x25 = double(x24)
    x26 = repeat(x21, x25)
    x27 = merge(x26)
    x28 = double(x17)
    x29 = repeat(x27, x28)
    x30 = asobject(x29)
    x31 = chain(increment, last, last)
    x32 = compose(first, last)
    x33 = fork(greater, x31, x32)
    x34 = sfilter(x30, x33)
    x35 = upscale(x16, TWO)
    x36 = dmirror(x34)
    x37 = combine(x34, x36)
    x38 = paint(x35, x37)
    x39 = x15(x38)
    return x39


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
