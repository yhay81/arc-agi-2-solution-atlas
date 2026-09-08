"""Executable re-arc DSL program for ARC-AGI-2 task 9aec4887.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    UNITY,
    F,
    T,
    argmax,
    backdrop,
    chain,
    color,
    colorfilter,
    compose,
    cover,
    equality,
    fgpartition,
    fork,
    greater,
    height,
    initset,
    lbind,
    manhattan,
    mapply,
    merge,
    mostcolor,
    multiply,
    normalize,
    objects,
    outbox,
    paint,
    rbind,
    recolor,
    remove,
    sfilter,
    shift,
    size,
    subgrid,
    toindices,
    valmin,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "9aec4887"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = fork(multiply, height, width)
    x2 = fork(equality, size, x1)
    x3 = sfilter(x0, x2)
    x4 = mostcolor(grid)
    x5 = colorfilter(x3, x4)
    x6 = argmax(x5, size)
    x7 = outbox(x6)
    x8 = backdrop(x7)
    x9 = subgrid(x8, grid)
    x10 = cover(grid, x8)
    x11 = fgpartition(x10)
    x12 = merge(x11)
    x13 = normalize(x12)
    x14 = shift(x13, UNITY)
    x15 = paint(x9, x14)
    x16 = toindices(x14)
    x17 = fgpartition(x9)
    x18 = rbind(remove, x17)
    x19 = lbind(lbind, manhattan)
    x20 = compose(x19, initset)
    x21 = lbind(fork, greater)
    x22 = lbind(sfilter, x16)
    x23 = rbind(compose, x20)
    x24 = lbind(lbind, valmin)
    x25 = chain(x23, x24, x18)
    x26 = rbind(compose, initset)
    x27 = lbind(rbind, manhattan)
    x28 = compose(x26, x27)
    x29 = fork(x21, x25, x28)
    x30 = compose(x22, x29)
    x31 = fork(recolor, color, x30)
    x32 = mapply(x31, x17)
    x33 = paint(x15, x32)
    return x33


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
