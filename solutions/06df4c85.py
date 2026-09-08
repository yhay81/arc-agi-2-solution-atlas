"""Executable re-arc DSL program for ARC-AGI-2 task 06df4c85.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    F,
    T,
    apply,
    asobject,
    chain,
    color,
    compose,
    connect,
    difference,
    either,
    flip,
    fork,
    frontiers,
    hline,
    identity,
    lbind,
    mapply,
    matcher,
    merge,
    mfilter,
    mostcolor,
    objects,
    paint,
    palette,
    prapply,
    rbind,
    recolor,
    sfilter,
    toindices,
    vline,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "06df4c85"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asobject(grid)
    x1 = frontiers(grid)
    x2 = merge(x1)
    x3 = difference(x0, x2)
    x4 = mostcolor(x3)
    x5 = objects(grid, T, F, F)
    x6 = color(x2)
    x7 = matcher(color, x6)
    x8 = matcher(color, x4)
    x9 = fork(either, x7, x8)
    x10 = compose(flip, x9)
    x11 = sfilter(x5, x10)
    x12 = merge(x11)
    x13 = palette(x12)
    x14 = lbind(mfilter, x11)
    x15 = lbind(matcher, color)
    x16 = compose(x14, x15)
    x17 = apply(x16, x13)
    x18 = fork(either, vline, hline)
    x19 = lbind(prapply, connect)
    x20 = fork(x19, identity, identity)
    x21 = compose(x20, toindices)
    x22 = rbind(sfilter, x18)
    x23 = chain(merge, x22, x21)
    x24 = fork(recolor, color, x23)
    x25 = mapply(x24, x17)
    x26 = paint(grid, x25)
    x27 = paint(x26, x2)
    return x27


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
