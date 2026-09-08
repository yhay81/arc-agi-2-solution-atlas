"""Executable re-arc DSL program for ARC-AGI-2 task 29623171.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ZERO,
    apply,
    asindices,
    astuple,
    canvas,
    colorcount,
    compose,
    compress,
    decrement,
    divide,
    fill,
    frontiers,
    height,
    hline,
    increment,
    lbind,
    leastcolor,
    matcher,
    mfilter,
    mostcolor,
    multiply,
    rbind,
    replace,
    sfilter,
    shift,
    size,
    subtract,
    toobject,
    valmax,
    vline,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "29623171"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = compress(grid)
    x1 = leastcolor(x0)
    x2 = mostcolor(x0)
    x3 = frontiers(grid)
    x4 = sfilter(x3, hline)
    x5 = size(x4)
    x6 = increment(x5)
    x7 = sfilter(x3, vline)
    x8 = size(x7)
    x9 = increment(x8)
    x10 = height(grid)
    x11 = decrement(x6)
    x12 = subtract(x10, x11)
    x13 = divide(x12, x6)
    x14 = width(grid)
    x15 = decrement(x9)
    x16 = subtract(x14, x15)
    x17 = divide(x16, x9)
    x18 = astuple(x13, x17)
    x19 = canvas(ZERO, x18)
    x20 = asindices(x19)
    x21 = astuple(x6, x9)
    x22 = canvas(ZERO, x21)
    x23 = asindices(x22)
    x24 = astuple(x13, x17)
    x25 = increment(x24)
    x26 = rbind(multiply, x25)
    x27 = apply(x26, x23)
    x28 = rbind(toobject, grid)
    x29 = lbind(shift, x20)
    x30 = compose(x28, x29)
    x31 = apply(x30, x27)
    x32 = rbind(colorcount, x1)
    x33 = valmax(x31, x32)
    x34 = rbind(colorcount, x1)
    x35 = matcher(x34, x33)
    x36 = mfilter(x31, x35)
    x37 = replace(grid, x1, x2)
    x38 = fill(x37, x1, x36)
    return x38


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
