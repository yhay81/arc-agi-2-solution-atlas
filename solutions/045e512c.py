"""Executable re-arc DSL program for ARC-AGI-2 task 045e512c.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ORIGIN,
    T,
    apply,
    argmax,
    argmin,
    astuple,
    chain,
    compose,
    crement,
    divide,
    equality,
    fork,
    height,
    increment,
    interval,
    lbind,
    mapply,
    maximum,
    mostcolor,
    multiply,
    neighbors,
    objects,
    paint,
    palette,
    rbind,
    recolor,
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

TASK_ID = "045e512c"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, T, T)
    x1 = argmax(x0, size)
    x2 = height(x1)
    x3 = width(x1)
    x4 = neighbors(ORIGIN)
    x5 = toindices(x1)
    x6 = lbind(shift, x5)
    x7 = height(grid)
    x8 = divide(x7, x2)
    x9 = width(grid)
    x10 = divide(x9, x3)
    x11 = astuple(x8, x10)
    x12 = maximum(x11)
    x13 = increment(x12)
    x14 = interval(ONE, x13, ONE)
    x15 = astuple(x2, x3)
    x16 = lbind(multiply, x15)
    x17 = compose(crement, x16)
    x18 = lbind(mapply, x6)
    x19 = rbind(apply, x14)
    x20 = lbind(rbind, multiply)
    x21 = compose(x20, x17)
    x22 = chain(x18, x19, x21)
    x23 = rbind(toobject, grid)
    x24 = compose(x6, x17)
    x25 = chain(palette, x23, x24)
    x26 = mostcolor(grid)
    x27 = rbind(equality, x26)
    x28 = rbind(argmin, x27)
    x29 = compose(x28, x25)
    x30 = fork(recolor, x29, x22)
    x31 = mapply(x30, x4)
    x32 = paint(grid, x31)
    return x32


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
