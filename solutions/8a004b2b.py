"""Executable re-arc DSL program for ARC-AGI-2 task 8a004b2b.

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
    apply,
    argmax,
    asobject,
    backdrop,
    colorcount,
    compose,
    contained,
    corners,
    difference,
    divide,
    equality,
    fgpartition,
    first,
    flip,
    fork,
    height,
    hupscale,
    identity,
    inbox,
    last,
    lbind,
    matcher,
    merge,
    mostcolor,
    mostcommon,
    order,
    paint,
    pair,
    palette,
    partition,
    rbind,
    sfilter,
    shift,
    size,
    subgrid,
    subtract,
    toindices,
    toobject,
    ulcorner,
    vupscale,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "8a004b2b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = fork(equality, toindices, corners)
    x2 = sfilter(x0, x1)
    x3 = argmax(x2, size)
    x4 = fgpartition(grid)
    x5 = merge(x4)
    x6 = backdrop(x3)
    x7 = toobject(x6, grid)
    x8 = difference(x5, x7)
    x9 = mostcolor(grid)
    x10 = inbox(x3)
    x11 = backdrop(x10)
    x12 = toobject(x11, grid)
    x13 = matcher(first, x9)
    x14 = compose(flip, x13)
    x15 = sfilter(x12, x14)
    x16 = subgrid(x8, grid)
    x17 = palette(x15)
    x18 = order(x17, identity)
    x19 = lbind(colorcount, x15)
    x20 = apply(x19, x18)
    x21 = lbind(colorcount, x8)
    x22 = apply(x21, x18)
    x23 = pair(x20, x22)
    x24 = fork(divide, first, last)
    x25 = apply(x24, x23)
    x26 = mostcommon(x25)
    x27 = lbind(colorcount, x15)
    x28 = lbind(colorcount, x8)
    x29 = fork(divide, x27, x28)
    x30 = matcher(x29, x26)
    x31 = palette(x8)
    x32 = sfilter(x31, x30)
    x33 = rbind(contained, x32)
    x34 = compose(x33, first)
    x35 = sfilter(x15, x34)
    x36 = sfilter(x8, x34)
    x37 = height(x35)
    x38 = height(x36)
    x39 = divide(x37, x38)
    x40 = width(x35)
    x41 = width(x36)
    x42 = divide(x40, x41)
    x43 = vupscale(x16, x39)
    x44 = hupscale(x43, x42)
    x45 = asobject(x44)
    x46 = matcher(first, x9)
    x47 = compose(flip, x46)
    x48 = sfilter(x45, x47)
    x49 = ulcorner(x15)
    x50 = sfilter(x48, x34)
    x51 = ulcorner(x50)
    x52 = subtract(x49, x51)
    x53 = shift(x48, x52)
    x54 = paint(grid, x53)
    x55 = subgrid(x3, x54)
    return x55


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
