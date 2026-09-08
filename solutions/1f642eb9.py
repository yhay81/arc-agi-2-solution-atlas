"""Executable re-arc DSL program for ARC-AGI-2 task 1f642eb9.

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
    asindices,
    color,
    combine,
    compose,
    corners,
    crement,
    difference,
    equality,
    fork,
    gravitate,
    height,
    identity,
    initset,
    mapply,
    multiply,
    objects,
    ofcolor,
    outbox,
    paint,
    rbind,
    sfilter,
    shift,
    size,
    toindices,
    toobject,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "1f642eb9"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = fork(multiply, height, width)
    x2 = fork(equality, size, x1)
    x3 = sfilter(x0, x2)
    x4 = argmax(x3, size)
    x5 = outbox(x4)
    x6 = corners(x5)
    x7 = toobject(x6, grid)
    x8 = color(x7)
    x9 = asindices(grid)
    x10 = ofcolor(grid, x8)
    x11 = toindices(x4)
    x12 = combine(x10, x11)
    x13 = difference(x9, x12)
    x14 = toobject(x13, grid)
    x15 = apply(initset, x14)
    x16 = rbind(gravitate, x4)
    x17 = compose(crement, x16)
    x18 = fork(shift, identity, x17)
    x19 = mapply(x18, x15)
    x20 = paint(grid, x19)
    return x20


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
