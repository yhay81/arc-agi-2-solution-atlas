"""Executable re-arc DSL program for ARC-AGI-2 task 2c608aff.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.re_arc_dsl import (
    add,
    apply,
    argmax,
    argmin,
    backdrop,
    color,
    colorcount,
    compose,
    connect,
    contained,
    either,
    equality,
    fill,
    first,
    fork,
    gravitate,
    identity,
    initset,
    last,
    lbind,
    mapply,
    ofcolor,
    palette,
    partition,
    rbind,
    remove,
    sfilter,
    size,
    toindices,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "2c608aff"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = fork(equality, toindices, backdrop)
    x2 = sfilter(x0, x1)
    x3 = argmax(x2, size)
    x4 = color(x3)
    x5 = palette(grid)
    x6 = remove(x4, x5)
    x7 = lbind(colorcount, grid)
    x8 = argmin(x6, x7)
    x9 = toindices(x3)
    x10 = apply(first, x9)
    x11 = toindices(x3)
    x12 = apply(last, x11)
    x13 = rbind(contained, x10)
    x14 = compose(x13, first)
    x15 = rbind(contained, x12)
    x16 = compose(x15, last)
    x17 = fork(either, x14, x16)
    x18 = ofcolor(grid, x8)
    x19 = sfilter(x18, x17)
    x20 = rbind(gravitate, x3)
    x21 = compose(x20, initset)
    x22 = fork(add, identity, x21)
    x23 = fork(connect, identity, x22)
    x24 = mapply(x23, x19)
    x25 = fill(grid, x8, x24)
    return x25


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
