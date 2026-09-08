"""Executable re-arc DSL program for ARC-AGI-2 task 29c11459.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    FIVE,
    ONE,
    TWO_BY_ZERO,
    F,
    T,
    add,
    apply,
    branch,
    center,
    chain,
    color,
    combine,
    compose,
    connect,
    crop,
    delta,
    either,
    equality,
    first,
    fork,
    halve,
    hline,
    hmatching,
    initset,
    last,
    lbind,
    matcher,
    merge,
    mfilter,
    mostcolor,
    numcolors,
    objects,
    paint,
    palette,
    product,
    rbind,
    recolor,
    remove,
    sfilter,
    shape,
    subtract,
    toobject,
    vline,
    vmatching,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "29c11459"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = product(x0, x0)
    x2 = fork(hmatching, first, last)
    x3 = fork(vmatching, first, last)
    x4 = fork(either, x2, x3)
    x5 = sfilter(x1, x4)
    x6 = mostcolor(grid)
    x7 = rbind(toobject, grid)
    x8 = compose(delta, merge)
    x9 = chain(palette, x7, x8)
    x10 = initset(x6)
    x11 = matcher(x9, x10)
    x12 = sfilter(x5, x11)
    x13 = shape(grid)
    x14 = subtract(x13, TWO_BY_ZERO)
    x15 = crop(grid, DOWN, x14)
    x16 = numcolors(x15)
    x17 = equality(ONE, x16)
    x18 = branch(x17, vline, hline)
    x19 = compose(center, first)
    x20 = compose(center, last)
    x21 = fork(add, x19, x20)
    x22 = compose(halve, x21)
    x23 = compose(color, first)
    x24 = compose(color, last)
    x25 = fork(connect, x19, x22)
    x26 = fork(remove, x22, x25)
    x27 = fork(recolor, x23, x26)
    x28 = fork(connect, x20, x22)
    x29 = fork(remove, x22, x28)
    x30 = fork(recolor, x24, x29)
    x31 = lbind(recolor, FIVE)
    x32 = chain(x31, initset, x22)
    x33 = fork(combine, x27, x30)
    x34 = fork(combine, x33, x32)
    x35 = apply(x34, x12)
    x36 = mfilter(x35, x18)
    x37 = paint(grid, x36)
    x38 = merge(x0)
    x39 = paint(x37, x38)
    return x39


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
