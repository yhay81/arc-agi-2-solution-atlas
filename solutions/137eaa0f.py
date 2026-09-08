"""Executable re-arc DSL program for ARC-AGI-2 task 137eaa0f.

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
    argmin,
    canvas,
    chain,
    color,
    colorcount,
    combine,
    compose,
    fgpartition,
    first,
    fork,
    identity,
    initset,
    invert,
    lbind,
    manhattan,
    mapply,
    matcher,
    merge,
    normalize,
    objects,
    ofcolor,
    paint,
    palette,
    rbind,
    recolor,
    remove,
    sfilter,
    shape,
    shift,
    size,
    totuple,
    ulcorner,
    valmax,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "137eaa0f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = merge(x0)
    x2 = palette(x1)
    x3 = objects(grid, T, F, T)
    x4 = totuple(x3)
    x5 = apply(color, x4)
    x6 = lbind(sfilter, x5)
    x7 = lbind(matcher, identity)
    x8 = chain(size, x6, x7)
    x9 = valmax(x2, x8)
    x10 = matcher(x8, x9)
    x11 = sfilter(x2, x10)
    x12 = lbind(colorcount, grid)
    x13 = argmin(x11, x12)
    x14 = ofcolor(grid, x13)
    x15 = recolor(x13, x14)
    x16 = apply(initset, x15)
    x17 = remove(x15, x0)
    x18 = lbind(argmin, x16)
    x19 = lbind(rbind, manhattan)
    x20 = compose(x18, x19)
    x21 = fork(combine, identity, x20)
    x22 = apply(x21, x17)
    x23 = matcher(first, x13)
    x24 = rbind(sfilter, x23)
    x25 = chain(invert, ulcorner, x24)
    x26 = fork(shift, identity, x25)
    x27 = mapply(x26, x22)
    x28 = normalize(x27)
    x29 = shape(x28)
    x30 = canvas(ZERO, x29)
    x31 = paint(x30, x28)
    return x31


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
