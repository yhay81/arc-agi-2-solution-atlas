"""Executable re-arc DSL program for ARC-AGI-2 task f8c80d96.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    FIVE,
    ONE,
    F,
    T,
    add,
    argmin,
    astuple,
    box,
    chain,
    color,
    colorfilter,
    compose,
    double,
    fill,
    fork,
    initset,
    insert,
    interval,
    lbind,
    leftmost,
    lowermost,
    lrcorner,
    manhattan,
    mapply,
    maximum,
    multiply,
    objects,
    other,
    palette,
    rbind,
    remove,
    replace,
    rightmost,
    shape,
    subtract,
    ulcorner,
    uppermost,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "f8c80d96"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = compose(maximum, shape)
    x2 = argmin(x0, x1)
    x3 = color(x2)
    x4 = palette(grid)
    x5 = other(x4, x3)
    x6 = colorfilter(x0, x5)
    x7 = argmin(x6, x1)
    x8 = remove(x7, x6)
    x9 = rbind(manhattan, x7)
    x10 = argmin(x8, x9)
    x11 = rightmost(x10)
    x12 = rightmost(x7)
    x13 = subtract(x11, x12)
    x14 = leftmost(x7)
    x15 = leftmost(x10)
    x16 = subtract(x14, x15)
    x17 = astuple(x13, x16)
    x18 = maximum(x17)
    x19 = lowermost(x10)
    x20 = lowermost(x7)
    x21 = subtract(x19, x20)
    x22 = uppermost(x7)
    x23 = uppermost(x10)
    x24 = subtract(x22, x23)
    x25 = astuple(x21, x24)
    x26 = maximum(x25)
    x27 = ulcorner(x7)
    x28 = lrcorner(x7)
    x29 = astuple(x26, x18)
    x30 = double(EIGHT)
    x31 = interval(ONE, x30, ONE)
    x32 = lbind(subtract, x27)
    x33 = rbind(multiply, x29)
    x34 = compose(x32, x33)
    x35 = lbind(add, x28)
    x36 = rbind(multiply, x29)
    x37 = chain(initset, x35, x36)
    x38 = fork(insert, x34, x37)
    x39 = compose(box, x38)
    x40 = mapply(x39, x31)
    x41 = fill(grid, x5, x40)
    x42 = replace(x41, x3, FIVE)
    return x42


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
