"""Executable re-arc DSL program for ARC-AGI-2 task 228f6490.

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
    argmax,
    bordering,
    chain,
    color,
    colorfilter,
    compose,
    cover,
    difference,
    flip,
    fork,
    identity,
    lbind,
    mapply,
    matcher,
    mostcolor,
    mostcommon,
    neighbors,
    normalize,
    objects,
    paint,
    rbind,
    recolor,
    sfilter,
    toindices,
    toobject,
    totuple,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "228f6490"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = objects(grid, T, T, F)
    x2 = colorfilter(x1, x0)
    x3 = compose(normalize, toindices)
    x4 = difference(x1, x2)
    x5 = rbind(bordering, grid)
    x6 = compose(flip, x5)
    x7 = sfilter(x2, x6)
    x8 = rbind(toobject, grid)
    x9 = lbind(mapply, neighbors)
    x10 = compose(x9, toindices)
    x11 = fork(difference, x10, identity)
    x12 = chain(mostcolor, x8, x11)
    x13 = totuple(x7)
    x14 = apply(x12, x13)
    x15 = mostcommon(x14)
    x16 = matcher(x12, x15)
    x17 = sfilter(x7, x16)
    x18 = lbind(argmax, x4)
    x19 = lbind(matcher, x3)
    x20 = chain(x18, x19, x3)
    x21 = compose(color, x20)
    x22 = fork(recolor, x21, identity)
    x23 = mapply(x20, x17)
    x24 = cover(grid, x23)
    x25 = mapply(x22, x17)
    x26 = paint(x24, x25)
    return x26


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
