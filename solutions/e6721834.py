"""Executable re-arc DSL program for ARC-AGI-2 task e6721834.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NEG_UNITY,
    TWO,
    UNITY,
    F,
    T,
    add,
    asobject,
    branch,
    canvas,
    chain,
    combine,
    compose,
    first,
    flip,
    fork,
    frontiers,
    greater,
    hline,
    hsplit,
    identity,
    last,
    lbind,
    mapply,
    matcher,
    merge,
    mostcolor,
    numcolors,
    objects,
    occurrences,
    order,
    outbox,
    paint,
    positive,
    rbind,
    recolor,
    sfilter,
    shape,
    shift,
    size,
    subtract,
    toindices,
    ulcorner,
    vline,
    vsplit,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "e6721834"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = sfilter(x0, hline)
    x2 = size(x1)
    x3 = sfilter(x0, vline)
    x4 = size(x3)
    x5 = greater(x2, x4)
    x6 = branch(x5, vsplit, hsplit)
    x7 = x6(grid, TWO)
    x8 = order(x7, numcolors)
    x9 = first(x8)
    x10 = last(x8)
    x11 = objects(x10, F, F, T)
    x12 = merge(x11)
    x13 = mostcolor(x12)
    x14 = matcher(first, x13)
    x15 = compose(flip, x14)
    x16 = rbind(sfilter, x15)
    x17 = mostcolor(x9)
    x18 = lbind(recolor, x17)
    x19 = rbind(sfilter, x14)
    x20 = compose(toindices, x19)
    x21 = fork(combine, x20, outbox)
    x22 = compose(x18, x21)
    x23 = fork(combine, x16, x22)
    x24 = shape(x9)
    x25 = add(TWO, x24)
    x26 = canvas(x17, x25)
    x27 = asobject(x9)
    x28 = shift(x27, UNITY)
    x29 = paint(x26, x28)
    x30 = rbind(shift, NEG_UNITY)
    x31 = lbind(occurrences, x29)
    x32 = compose(x30, x31)
    x33 = compose(x32, x23)
    x34 = chain(positive, size, x33)
    x35 = sfilter(x11, x34)
    x36 = chain(first, x32, x23)
    x37 = compose(ulcorner, x23)
    x38 = fork(subtract, x36, x37)
    x39 = fork(shift, identity, x38)
    x40 = mapply(x39, x35)
    x41 = paint(x9, x40)
    return x41


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
