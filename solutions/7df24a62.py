"""Executable re-arc DSL program for ARC-AGI-2 task 7df24a62.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    UNITY,
    apply,
    argmin,
    asobject,
    astuple,
    backdrop,
    canvas,
    chain,
    cmirror,
    color,
    colorcount,
    combine,
    compose,
    dmirror,
    first,
    fork,
    hmirror,
    identity,
    increment,
    initset,
    last,
    lbind,
    mapply,
    matcher,
    maximum,
    mostcolor,
    normalize,
    occurrences,
    ofcolor,
    paint,
    palette,
    partition,
    product,
    rapply,
    rbind,
    recolor,
    remove,
    repeat,
    sfilter,
    shape,
    shift,
    toobject,
    trim,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "7df24a62"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = compose(maximum, shape)
    x2 = argmin(x0, x1)
    x3 = color(x2)
    x4 = palette(grid)
    x5 = remove(x3, x4)
    x6 = lbind(colorcount, grid)
    x7 = argmin(x5, x6)
    x8 = mostcolor(grid)
    x9 = shape(grid)
    x10 = increment(x9)
    x11 = increment(x10)
    x12 = canvas(x8, x11)
    x13 = asobject(grid)
    x14 = shift(x13, UNITY)
    x15 = paint(x12, x14)
    x16 = repeat(identity, ONE)
    x17 = astuple(cmirror, dmirror)
    x18 = astuple(hmirror, vmirror)
    x19 = combine(x17, x18)
    x20 = combine(x16, x19)
    x21 = fork(compose, first, last)
    x22 = product(x20, x20)
    x23 = apply(x21, x22)
    x24 = ofcolor(x15, x3)
    x25 = backdrop(x24)
    x26 = toobject(x25, x15)
    x27 = matcher(first, x7)
    x28 = rbind(sfilter, x27)
    x29 = matcher(first, x3)
    x30 = rbind(sfilter, x29)
    x31 = lbind(recolor, x8)
    x32 = compose(x31, x30)
    x33 = fork(combine, x28, x32)
    x34 = lbind(lbind, shift)
    x35 = lbind(occurrences, x15)
    x36 = compose(x35, x33)
    x37 = fork(mapply, x34, x36)
    x38 = lbind(chain, x37)
    x39 = lbind(x38, normalize)
    x40 = rbind(rapply, x26)
    x41 = initset(x39)
    x42 = lbind(rapply, x41)
    x43 = chain(first, x40, x42)
    x44 = mapply(x43, x23)
    x45 = paint(x15, x44)
    x46 = trim(x45)
    return x46


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
