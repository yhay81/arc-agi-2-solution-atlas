"""Executable re-arc DSL program for ARC-AGI-2 task 447fd412.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    SIX,
    THREE,
    F,
    T,
    apply,
    argmax,
    argmin,
    asobject,
    canvas,
    chain,
    colorcount,
    combine,
    compose,
    equality,
    first,
    fork,
    identity,
    intersection,
    interval,
    lbind,
    mapply,
    matcher,
    merge,
    mfilter,
    mostcolor,
    multiply,
    normalize,
    numcolors,
    objects,
    occurrences,
    paint,
    palette,
    positive,
    rbind,
    recolor,
    remove,
    sfilter,
    shape,
    shift,
    size,
    subgrid,
    toindices,
    upscale,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "447fd412"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asobject(grid)
    x1 = shape(grid)
    x2 = shift(x0, x1)
    x3 = mostcolor(grid)
    x4 = shape(grid)
    x5 = multiply(x4, THREE)
    x6 = canvas(x3, x5)
    x7 = paint(x6, x2)
    x8 = objects(x7, F, T, T)
    x9 = argmax(x8, numcolors)
    x10 = normalize(x9)
    x11 = remove(x10, x8)
    x12 = merge(x11)
    x13 = mostcolor(x12)
    x14 = palette(x10)
    x15 = matcher(identity, x13)
    x16 = argmin(x14, x15)
    x17 = matcher(first, x13)
    x18 = sfilter(x10, x17)
    x19 = matcher(first, x16)
    x20 = sfilter(x10, x19)
    x21 = recolor(x3, x20)
    x22 = combine(x18, x21)
    x23 = lbind(mfilter, x8)
    x24 = lbind(occurrences, x7)
    x25 = lbind(upscale, x22)
    x26 = compose(x24, x25)
    x27 = lbind(lbind, shift)
    x28 = lbind(upscale, x10)
    x29 = compose(x27, x28)
    x30 = fork(apply, x29, x26)
    x31 = compose(positive, size)
    x32 = lbind(chain, x31)
    x33 = rbind(x32, toindices)
    x34 = lbind(rbind, intersection)
    x35 = chain(x23, x33, x34)
    x36 = chain(size, x35, toindices)
    x37 = rbind(colorcount, x13)
    x38 = fork(equality, x36, x37)
    x39 = rbind(sfilter, x38)
    x40 = chain(merge, x39, x30)
    x41 = interval(ONE, SIX, ONE)
    x42 = mapply(x40, x41)
    x43 = paint(x7, x42)
    x44 = subgrid(x2, x43)
    return x44


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
