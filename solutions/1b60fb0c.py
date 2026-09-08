"""Executable re-arc DSL program for ARC-AGI-2 task 1b60fb0c.

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
    argmax,
    backdrop,
    canvas,
    center,
    chain,
    combine,
    compose,
    difference,
    equality,
    fgpartition,
    fill,
    fork,
    increment,
    intersection,
    invert,
    lbind,
    mapply,
    maximum,
    minimum,
    normalize,
    ofcolor,
    outbox,
    paint,
    power,
    rbind,
    recolor,
    rot90,
    sfilter,
    shape,
    shift,
    size,
    subtract,
    toindices,
    ulcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "1b60fb0c"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = mapply(toindices, x0)
    x2 = rot90(grid)
    x3 = fgpartition(x2)
    x4 = mapply(toindices, x3)
    x5 = normalize(x4)
    x6 = ulcorner(x1)
    x7 = shift(x5, x6)
    x8 = shape(x1)
    x9 = maximum(x8)
    x10 = minimum(x8)
    x11 = subtract(x9, x10)
    x12 = increment(x11)
    x13 = power(outbox, x12)
    x14 = center(x7)
    x15 = x13(x7)
    x16 = backdrop(x15)
    x17 = invert(x14)
    x18 = shift(x16, x17)
    x19 = lbind(combine, x1)
    x20 = lbind(shift, x7)
    x21 = compose(x19, x20)
    x22 = rbind(ofcolor, ONE)
    x23 = lbind(canvas, ZERO)
    x24 = chain(x23, shape, x21)
    x25 = lbind(recolor, ONE)
    x26 = chain(x25, normalize, x21)
    x27 = fork(paint, x24, x26)
    x28 = chain(x22, rot90, x27)
    x29 = compose(normalize, x21)
    x30 = fork(equality, x29, x28)
    x31 = sfilter(x18, x30)
    x32 = lbind(intersection, x1)
    x33 = lbind(shift, x7)
    x34 = chain(size, x32, x33)
    x35 = argmax(x31, x34)
    x36 = shift(x7, x35)
    x37 = difference(x36, x1)
    x38 = fill(grid, TWO, x37)
    return x38


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
