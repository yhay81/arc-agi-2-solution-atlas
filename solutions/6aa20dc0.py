"""Executable re-arc DSL program for ARC-AGI-2 task 6aa20dc0.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FIVE,
    ONE,
    TWO,
    UNITY,
    F,
    T,
    add,
    asobject,
    backdrop,
    canvas,
    chain,
    cmirror,
    combine,
    compose,
    difference,
    dmirror,
    dneighbors,
    first,
    flip,
    fork,
    hmirror,
    identity,
    initset,
    insert,
    interval,
    last,
    lbind,
    mapply,
    matcher,
    mfilter,
    mostcolor,
    normalize,
    numcolors,
    objects,
    occurrences,
    paint,
    product,
    rapply,
    rbind,
    recolor,
    sfilter,
    shape,
    shift,
    toindices,
    toobject,
    ulcorner,
    upscale,
    valmax,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "6aa20dc0"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, T, T)
    x1 = mostcolor(grid)
    x2 = valmax(x0, numcolors)
    x3 = matcher(numcolors, x2)
    x4 = mfilter(x0, x3)
    x5 = backdrop(x4)
    x6 = toobject(x5, grid)
    x7 = matcher(first, x1)
    x8 = compose(flip, x7)
    x9 = sfilter(x6, x8)
    x10 = mostcolor(x9)
    x11 = initset(identity)
    x12 = insert(dmirror, x11)
    x13 = insert(cmirror, x12)
    x14 = insert(hmirror, x13)
    x15 = insert(vmirror, x14)
    x16 = shape(grid)
    x17 = add(TWO, x16)
    x18 = canvas(x1, x17)
    x19 = asobject(grid)
    x20 = shift(x19, UNITY)
    x21 = paint(x18, x20)
    x22 = interval(ONE, FIVE, ONE)
    x23 = matcher(first, x10)
    x24 = compose(flip, x23)
    x25 = rbind(sfilter, x24)
    x26 = compose(normalize, x25)
    x27 = chain(normalize, toindices, x26)
    x28 = lbind(upscale, x9)
    x29 = compose(initset, last)
    x30 = compose(x28, first)
    x31 = fork(rapply, x29, x30)
    x32 = chain(normalize, first, x31)
    x33 = compose(normalize, x26)
    x34 = lbind(recolor, x1)
    x35 = lbind(mapply, dneighbors)
    x36 = compose(x35, x27)
    x37 = fork(difference, x36, x27)
    x38 = compose(x34, x37)
    x39 = fork(combine, x33, x38)
    x40 = compose(x39, x32)
    x41 = lbind(lbind, shift)
    x42 = chain(ulcorner, x26, x32)
    x43 = fork(shift, x32, x42)
    x44 = compose(x41, x43)
    x45 = lbind(occurrences, x21)
    x46 = compose(x45, x40)
    x47 = fork(mapply, x44, x46)
    x48 = product(x22, x15)
    x49 = mapply(x47, x48)
    x50 = paint(grid, x49)
    return x50


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
