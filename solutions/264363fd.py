"""Executable re-arc DSL program for ARC-AGI-2 task 264363fd.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    TWO,
    F,
    T,
    argmax,
    argmin,
    asobject,
    backdrop,
    canvas,
    center,
    chain,
    color,
    combine,
    compose,
    cover,
    difference,
    dneighbors,
    extract,
    first,
    fork,
    greater,
    hconcat,
    height,
    identity,
    initset,
    intersection,
    invert,
    last,
    lbind,
    mapply,
    matcher,
    mostcolor,
    multiply,
    normalize,
    objects,
    ofcolor,
    outbox,
    paint,
    power,
    rbind,
    recolor,
    remove,
    sfilter,
    shape,
    shift,
    shoot,
    size,
    subgrid,
    toindices,
    ulcorner,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "264363fd"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = fork(multiply, height, width)
    x2 = argmax(x0, x1)
    x3 = mostcolor(x2)
    x4 = shape(grid)
    x5 = canvas(x3, x4)
    x6 = hconcat(grid, x5)
    x7 = objects(x6, F, F, T)
    x8 = argmin(x7, size)
    x9 = cover(grid, x8)
    x10 = normalize(x8)
    x11 = remove(x8, x7)
    x12 = toindices(x10)
    x13 = lbind(intersection, x12)
    x14 = chain(x13, dneighbors, last)
    x15 = rbind(greater, ONE)
    x16 = chain(x15, size, x14)
    x17 = sfilter(x10, x16)
    x18 = center(x17)
    x19 = matcher(last, x18)
    x20 = extract(x17, x19)
    x21 = first(x20)
    x22 = difference(x10, x17)
    x23 = color(x22)
    x24 = center(x17)
    x25 = invert(x24)
    x26 = shift(x10, x25)
    x27 = invert(x24)
    x28 = shift(x22, x27)
    x29 = toindices(x28)
    x30 = rbind(mapply, x29)
    x31 = lbind(lbind, shoot)
    x32 = compose(x30, x31)
    x33 = power(outbox, TWO)
    x34 = chain(backdrop, x33, initset)
    x35 = fork(difference, x32, x34)
    x36 = lbind(recolor, x23)
    x37 = compose(x36, x35)
    x38 = lbind(shift, x26)
    x39 = fork(combine, x37, x38)
    x40 = lbind(mapply, x39)
    x41 = rbind(ofcolor, x21)
    x42 = compose(x40, x41)
    x43 = fork(paint, identity, x42)
    x44 = rbind(subgrid, grid)
    x45 = chain(asobject, x43, x44)
    x46 = fork(shift, x45, ulcorner)
    x47 = mapply(x46, x11)
    x48 = paint(x9, x47)
    return x48


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
