"""Executable re-arc DSL program for ARC-AGI-2 task b190f7f5.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    TWO,
    add,
    apply,
    argmax,
    argmin,
    asindices,
    asobject,
    astuple,
    canvas,
    chain,
    compose,
    contained,
    dedupe,
    difference,
    first,
    flip,
    fork,
    hsplit,
    intersection,
    last,
    lbind,
    mapply,
    matcher,
    minimum,
    multiply,
    numcolors,
    ofcolor,
    paint,
    palette,
    recolor,
    sfilter,
    shape,
    shift,
    size,
    vsplit,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "b190f7f5"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = lbind(contained, TWO)
    x1 = lbind(apply, numcolors)
    x2 = compose(x0, x1)
    x3 = lbind(apply, shape)
    x4 = chain(size, dedupe, x3)
    x5 = matcher(x4, ONE)
    x6 = compose(palette, first)
    x7 = compose(palette, last)
    x8 = fork(intersection, x6, x7)
    x9 = compose(size, x8)
    x10 = matcher(x9, ONE)
    x11 = lbind(contained, ONE)
    x12 = compose(minimum, shape)
    x13 = lbind(apply, x12)
    x14 = chain(flip, x11, x13)
    x15 = fork(add, x2, x5)
    x16 = fork(add, x10, x14)
    x17 = fork(add, x15, x16)
    x18 = vsplit(grid, TWO)
    x19 = hsplit(grid, TWO)
    x20 = astuple(x18, x19)
    x21 = argmax(x20, x17)
    x22 = argmin(x21, numcolors)
    x23 = argmax(x21, numcolors)
    x24 = palette(x22)
    x25 = palette(x23)
    x26 = intersection(x24, x25)
    x27 = first(x26)
    x28 = asindices(x22)
    x29 = ofcolor(x22, x27)
    x30 = difference(x28, x29)
    x31 = asobject(x23)
    x32 = matcher(first, x27)
    x33 = sfilter(x31, x32)
    x34 = difference(x31, x33)
    x35 = shape(x22)
    x36 = multiply(x35, x35)
    x37 = canvas(x27, x36)
    x38 = lbind(shift, x30)
    x39 = lbind(multiply, x35)
    x40 = chain(x38, x39, last)
    x41 = fork(recolor, first, x40)
    x42 = mapply(x41, x34)
    x43 = paint(x37, x42)
    return x43


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
