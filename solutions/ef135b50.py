"""Executable re-arc DSL program for ARC-AGI-2 task ef135b50.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NEG_ONE,
    NINE,
    F,
    T,
    argmax,
    asindices,
    backdrop,
    box,
    chain,
    color,
    compose,
    difference,
    equality,
    fill,
    flip,
    fork,
    height,
    identity,
    intersection,
    lbind,
    mapply,
    multiply,
    objects,
    ofcolor,
    paint,
    rbind,
    recolor,
    sfilter,
    size,
    vsplit,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "ef135b50"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = fork(multiply, height, width)
    x2 = fork(equality, size, x1)
    x3 = compose(flip, x2)
    x4 = sfilter(x0, x3)
    x5 = argmax(x4, x1)
    x6 = color(x5)
    x7 = ofcolor(grid, x6)
    x8 = asindices(grid)
    x9 = difference(x8, x7)
    x10 = fill(grid, NEG_ONE, x9)
    x11 = lbind(recolor, NEG_ONE)
    x12 = rbind(ofcolor, NEG_ONE)
    x13 = chain(x11, backdrop, x12)
    x14 = fork(paint, identity, x13)
    x15 = height(x10)
    x16 = vsplit(x10, x15)
    x17 = mapply(x14, x16)
    x18 = ofcolor(x17, NEG_ONE)
    x19 = asindices(grid)
    x20 = box(x19)
    x21 = difference(x18, x20)
    x22 = intersection(x21, x7)
    x23 = fill(grid, NINE, x22)
    return x23


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
