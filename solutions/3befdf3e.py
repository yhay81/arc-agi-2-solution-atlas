"""Executable re-arc DSL program for ARC-AGI-2 task 3befdf3e.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    F,
    T,
    backdrop,
    box,
    chain,
    color,
    combine,
    compose,
    contained,
    decrement,
    difference,
    fork,
    height,
    identity,
    invert,
    last,
    lbind,
    mapply,
    objects,
    other,
    paint,
    palette,
    rbind,
    recolor,
    sfilter,
    shift,
    toindices,
    toivec,
    tojvec,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "3befdf3e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, F, T)
    x1 = rbind(compose, last)
    x2 = lbind(rbind, contained)
    x3 = chain(x1, x2, box)
    x4 = fork(sfilter, identity, x3)
    x5 = compose(color, x4)
    x6 = fork(other, palette, x5)
    x7 = chain(decrement, decrement, height)
    x8 = chain(decrement, decrement, width)
    x9 = compose(toivec, x7)
    x10 = fork(shift, toindices, x9)
    x11 = chain(toivec, invert, x7)
    x12 = fork(shift, toindices, x11)
    x13 = compose(tojvec, x8)
    x14 = fork(shift, toindices, x13)
    x15 = chain(tojvec, invert, x8)
    x16 = fork(shift, toindices, x15)
    x17 = fork(combine, x10, x12)
    x18 = fork(combine, x14, x16)
    x19 = fork(combine, x17, x18)
    x20 = fork(combine, backdrop, x19)
    x21 = fork(difference, x20, box)
    x22 = fork(recolor, x5, x21)
    x23 = fork(recolor, x6, box)
    x24 = fork(combine, x22, x23)
    x25 = mapply(x24, x0)
    x26 = paint(grid, x25)
    return x26


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
