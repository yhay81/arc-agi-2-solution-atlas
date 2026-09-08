"""Executable re-arc DSL program for ARC-AGI-2 task 5521c0d9.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ZERO,
    F,
    T,
    apply,
    asindices,
    astuple,
    box,
    canvas,
    chain,
    cmirror,
    combine,
    compose,
    dmirror,
    extract,
    fill,
    first,
    fork,
    hconcat,
    height,
    hmirror,
    identity,
    initset,
    lbind,
    mapply,
    matcher,
    maximum,
    merge,
    mostcolor,
    objects,
    paint,
    rapply,
    rbind,
    shape,
    shift,
    toivec,
    toobject,
    uppermost,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "5521c0d9"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asindices(grid)
    x1 = box(x0)
    x2 = toobject(x1, grid)
    x3 = mostcolor(x2)
    x4 = rbind(objects, T)
    x5 = rbind(x4, F)
    x6 = rbind(x5, T)
    x7 = lbind(canvas, x3)
    x8 = compose(x7, shape)
    x9 = fork(hconcat, identity, x8)
    x10 = compose(x6, x9)
    x11 = lbind(apply, uppermost)
    x12 = chain(maximum, x11, x10)
    x13 = matcher(x12, ZERO)
    x14 = astuple(identity, dmirror)
    x15 = astuple(cmirror, hmirror)
    x16 = combine(x14, x15)
    x17 = rbind(rapply, grid)
    x18 = chain(first, x17, initset)
    x19 = compose(x13, x18)
    x20 = extract(x16, x19)
    x21 = x20(grid)
    x22 = shape(x21)
    x23 = canvas(x3, x22)
    x24 = hconcat(x21, x23)
    x25 = objects(x24, T, F, T)
    x26 = compose(toivec, height)
    x27 = fork(shift, identity, x26)
    x28 = mapply(x27, x25)
    x29 = mostcolor(grid)
    x30 = merge(x25)
    x31 = fill(x21, x29, x30)
    x32 = paint(x31, x28)
    x33 = x20(x32)
    return x33


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
