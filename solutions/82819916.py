"""Executable re-arc DSL program for ARC-AGI-2 task 82819916.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    apply,
    argmin,
    asobject,
    branch,
    chain,
    color,
    combine,
    compose,
    contained,
    difference,
    dmirror,
    fgpartition,
    first,
    fork,
    frontiers,
    hline,
    identity,
    last,
    lbind,
    mapply,
    matcher,
    merge,
    mostcolor,
    other,
    paint,
    palette,
    positive,
    rbind,
    recolor,
    repeat,
    sfilter,
    shift,
    size,
    toindices,
    toivec,
    totuple,
    uppermost,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "82819916"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = sfilter(x0, hline)
    x2 = size(x1)
    x3 = positive(x2)
    x4 = branch(x3, identity, dmirror)
    x5 = x4(grid)
    x6 = frontiers(grid)
    x7 = merge(x6)
    x8 = mostcolor(x7)
    x9 = matcher(identity, x8)
    x10 = rbind(sfilter, x9)
    x11 = compose(size, x10)
    x12 = argmin(x5, x11)
    x13 = repeat(x12, ONE)
    x14 = asobject(x13)
    x15 = palette(x14)
    x16 = totuple(x15)
    x17 = first(x16)
    last(x16)
    x19 = fgpartition(x5)
    x20 = merge(x19)
    x21 = toindices(x20)
    x22 = apply(first, x21)
    x23 = lbind(sfilter, x20)
    x24 = compose(first, last)
    x25 = lbind(matcher, x24)
    x26 = compose(x23, x25)
    x27 = apply(x26, x22)
    x28 = lbind(shift, x14)
    x29 = chain(x28, toivec, uppermost)
    x30 = matcher(first, x17)
    x31 = rbind(sfilter, x30)
    x32 = rbind(compose, last)
    x33 = lbind(rbind, contained)
    x34 = chain(toindices, x31, x29)
    x35 = chain(x32, x33, x34)
    x36 = fork(sfilter, identity, x35)
    x37 = compose(color, x36)
    x38 = compose(x31, x29)
    x39 = fork(recolor, x37, x38)
    x40 = fork(other, palette, x37)
    x41 = compose(x31, x29)
    x42 = fork(difference, x29, x41)
    x43 = fork(recolor, x40, x42)
    x44 = fork(combine, x39, x43)
    x45 = mapply(x44, x27)
    x46 = paint(x5, x45)
    x47 = x4(x46)
    return x47


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
