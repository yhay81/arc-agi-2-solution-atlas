"""Executable re-arc DSL program for ARC-AGI-2 task f35d900a.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FIVE,
    F,
    T,
    argmin,
    box,
    chain,
    color,
    compose,
    difference,
    even,
    fill,
    fork,
    initset,
    lbind,
    manhattan,
    mapply,
    mostcolor,
    objects,
    other,
    outbox,
    paint,
    palette,
    rbind,
    recolor,
    remove,
    sfilter,
    toindices,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "f35d900a"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = palette(grid)
    x2 = mostcolor(grid)
    x3 = remove(x2, x1)
    x4 = lbind(other, x3)
    x5 = compose(x4, color)
    x6 = fork(recolor, x5, outbox)
    x7 = mapply(x6, x0)
    x8 = mapply(toindices, x0)
    x9 = box(x8)
    x10 = difference(x9, x8)
    x11 = lbind(argmin, x8)
    x12 = rbind(compose, initset)
    x13 = lbind(rbind, manhattan)
    x14 = chain(x12, x13, initset)
    x15 = chain(initset, x11, x14)
    x16 = fork(manhattan, initset, x15)
    x17 = compose(even, x16)
    x18 = sfilter(x10, x17)
    x19 = paint(grid, x7)
    x20 = fill(x19, FIVE, x18)
    return x20


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
