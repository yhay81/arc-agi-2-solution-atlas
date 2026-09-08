"""Executable re-arc DSL program for ARC-AGI-2 task 3618c87e.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ZERO,
    F,
    T,
    apply,
    astuple,
    branch,
    color,
    decrement,
    dedupe,
    dmirror,
    either,
    equality,
    fill,
    first,
    height,
    last,
    lbind,
    mostcolor,
    mostcommon,
    objects,
    ofcolor,
    other,
    palette,
    rbind,
    remove,
    repeat,
    replace,
    sizefilter,
    totuple,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "3618c87e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = objects(grid, T, F, F)
    x2 = sizefilter(x1, ONE)
    x3 = totuple(x2)
    x4 = apply(color, x3)
    x5 = mostcommon(x4)
    x6 = palette(grid)
    x7 = remove(x5, x6)
    x8 = other(x7, x0)
    x9 = replace(grid, x5, x0)
    x10 = ofcolor(grid, x5)
    x11 = repeat(x8, ONE)
    x12 = rbind(equality, x11)
    x13 = first(grid)
    x14 = dedupe(x13)
    x15 = x12(x14)
    x16 = last(grid)
    x17 = dedupe(x16)
    x18 = x12(x17)
    x19 = dmirror(grid)
    x20 = first(x19)
    x21 = dedupe(x20)
    x22 = x12(x21)
    x23 = dmirror(grid)
    x24 = last(x23)
    x25 = dedupe(x24)
    x12(x25)
    x27 = apply(last, x10)
    x28 = apply(first, x10)
    x29 = either(x15, x18)
    x30 = branch(x29, x27, x28)
    x31 = branch(x29, lbind, rbind)
    x32 = lbind(x31, astuple)
    x33 = branch(x29, height, width)
    x34 = x33(grid)
    x35 = decrement(x34)
    x36 = either(x15, x22)
    x37 = branch(x36, ZERO, x35)
    x38 = x32(x37)
    x39 = apply(x38, x30)
    x40 = fill(x9, x5, x39)
    return x40


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
