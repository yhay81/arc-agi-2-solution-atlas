"""Executable re-arc DSL program for ARC-AGI-2 task d43fd935.

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
    asobject,
    center,
    color,
    compose,
    connect,
    difference,
    either,
    equality,
    first,
    flip,
    fork,
    gravitate,
    height,
    hmatching,
    initset,
    mapply,
    matcher,
    mostcolor,
    multiply,
    paint,
    partition,
    rbind,
    recolor,
    sfilter,
    size,
    vmatching,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d43fd935"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = asobject(grid)
    x2 = matcher(first, x0)
    x3 = compose(flip, x2)
    x4 = sfilter(x1, x3)
    x5 = partition(grid)
    x6 = fork(multiply, height, width)
    x7 = fork(equality, size, x6)
    x8 = sfilter(x5, x7)
    x9 = argmax(x8, size)
    x10 = difference(x4, x9)
    x11 = apply(initset, x10)
    x12 = rbind(hmatching, x9)
    x13 = rbind(vmatching, x9)
    x14 = fork(either, x12, x13)
    x15 = sfilter(x11, x14)
    x16 = rbind(gravitate, x9)
    x17 = fork(add, center, x16)
    x18 = fork(connect, center, x17)
    x19 = fork(recolor, color, x18)
    x20 = mapply(x19, x15)
    x21 = paint(grid, x20)
    return x21


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
