"""Executable re-arc DSL program for ARC-AGI-2 task 5168d44c.

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
    add,
    apply,
    argmax,
    argmin,
    astuple,
    branch,
    chain,
    color,
    colorfilter,
    combine,
    compose,
    delta,
    equality,
    first,
    fork,
    height,
    hmirror,
    last,
    lbind,
    leftmost,
    lowermost,
    manhattan,
    matcher,
    maximum,
    multiply,
    objects,
    other,
    paint,
    partition,
    remove,
    replace,
    rightmost,
    sfilter,
    shift,
    size,
    subtract,
    ulcorner,
    uppermost,
    valmax,
    vmirror,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "5168d44c"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = fork(multiply, height, width)
    x2 = valmax(x0, x1)
    x3 = matcher(x1, x2)
    x4 = sfilter(x0, x3)
    x5 = argmax(x4, size)
    x6 = color(x5)
    x7 = remove(x5, x0)
    x8 = objects(grid, T, F, F)
    x9 = lbind(colorfilter, x8)
    x10 = chain(size, x9, color)
    x11 = argmin(x7, x10)
    x12 = other(x7, x11)
    x13 = color(x12)
    x14 = colorfilter(x8, x13)
    x15 = apply(leftmost, x14)
    x16 = size(x15)
    x17 = equality(ONE, x16)
    x18 = apply(uppermost, x14)
    x19 = size(x18)
    x20 = equality(ONE, x19)
    x21 = fork(add, first, last)
    x22 = compose(x21, ulcorner)
    x23 = argmin(x14, x22)
    x24 = remove(x23, x14)
    x25 = lbind(manhattan, x23)
    x26 = argmin(x24, x25)
    x27 = lowermost(x26)
    x28 = lowermost(x23)
    x29 = subtract(x27, x28)
    x30 = uppermost(x26)
    x31 = uppermost(x23)
    x32 = subtract(x30, x31)
    x33 = astuple(x29, x32)
    x34 = maximum(x33)
    x35 = branch(x20, ZERO, x34)
    x36 = rightmost(x26)
    x37 = rightmost(x23)
    x38 = subtract(x36, x37)
    x39 = leftmost(x26)
    x40 = leftmost(x23)
    x41 = subtract(x39, x40)
    x42 = astuple(x38, x41)
    x43 = maximum(x42)
    x44 = branch(x17, ZERO, x43)
    x45 = astuple(x35, x44)
    x46 = shift(x11, x45)
    x47 = delta(x46)
    x48 = hmirror(x46)
    x49 = ulcorner(x47)
    x50 = delta(x48)
    x51 = ulcorner(x50)
    x52 = subtract(x49, x51)
    x53 = shift(x48, x52)
    x54 = combine(x46, x53)
    x55 = vmirror(x54)
    x56 = ulcorner(x47)
    x57 = delta(x55)
    x58 = ulcorner(x57)
    x59 = subtract(x56, x58)
    x60 = shift(x55, x59)
    x61 = combine(x60, x54)
    x62 = color(x11)
    x63 = replace(grid, x62, x6)
    x64 = paint(x63, x61)
    return x64


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
