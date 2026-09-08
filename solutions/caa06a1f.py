"""Executable re-arc DSL program for ARC-AGI-2 task caa06a1f.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    LEFT,
    ONE,
    ORIGIN,
    RIGHT,
    TWO,
    UP,
    add,
    apply,
    asindices,
    asobject,
    box,
    compose,
    equality,
    first,
    flip,
    height,
    hperiod,
    index,
    interval,
    invert,
    lbind,
    llcorner,
    lrcorner,
    mapply,
    matcher,
    mostcolor,
    multiply,
    paint,
    product,
    rbind,
    sfilter,
    shift,
    subtract,
    toobject,
    urcorner,
    vperiod,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "caa06a1f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asindices(grid)
    x1 = box(x0)
    x2 = toobject(x1, grid)
    x3 = mostcolor(x2)
    x4 = asobject(grid)
    x5 = matcher(first, x3)
    x6 = compose(flip, x5)
    x7 = sfilter(x4, x6)
    x8 = hperiod(x7)
    x9 = vperiod(x7)
    x10 = width(grid)
    x11 = width(x7)
    x12 = subtract(x10, x11)
    x13 = add(x12, TWO)
    x14 = height(grid)
    x15 = height(x7)
    x16 = subtract(x14, x15)
    x17 = add(x16, TWO)
    x18 = rbind(multiply, x8)
    x19 = invert(x13)
    x20 = interval(x19, x13, ONE)
    x21 = apply(x18, x20)
    x22 = rbind(multiply, x9)
    x23 = invert(x17)
    x24 = interval(x23, x17, ONE)
    x25 = apply(x22, x24)
    x26 = product(x25, x21)
    x27 = lbind(shift, x7)
    x28 = mapply(x27, x26)
    x29 = index(grid, ORIGIN)
    x30 = equality(x29, x3)
    x31 = flip(x30)
    x32 = asindices(grid)
    x33 = urcorner(x32)
    x34 = index(grid, x33)
    x35 = equality(x34, x3)
    x36 = flip(x35)
    x37 = asindices(grid)
    x38 = lrcorner(x37)
    x39 = index(grid, x38)
    x40 = equality(x39, x3)
    x41 = flip(x40)
    x42 = asindices(grid)
    x43 = llcorner(x42)
    x44 = index(grid, x43)
    x45 = equality(x44, x3)
    x46 = flip(x45)
    x47 = multiply(x31, LEFT)
    x48 = multiply(x36, UP)
    x49 = add(x47, x48)
    x50 = multiply(x41, RIGHT)
    x51 = multiply(x46, DOWN)
    x52 = add(x50, x51)
    x53 = add(x49, x52)
    x54 = shift(x28, x53)
    x55 = paint(grid, x54)
    return x55


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
