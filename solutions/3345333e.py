"""Executable re-arc DSL program for ARC-AGI-2 task 3345333e.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ZERO,
    argmax,
    asindices,
    astuple,
    box,
    chain,
    color,
    combine,
    equality,
    extract,
    fill,
    first,
    fork,
    halve,
    height,
    hmirror,
    increment,
    initset,
    insert,
    intersection,
    interval,
    invert,
    last,
    matcher,
    maximum,
    mostcolor,
    multiply,
    ofcolor,
    other,
    palette,
    partition,
    product,
    rbind,
    remove,
    sfilter,
    shift,
    size,
    toindices,
    toobject,
    vmirror,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "3345333e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asindices(grid)
    x1 = box(x0)
    x2 = toobject(x1, grid)
    x3 = mostcolor(x2)
    x4 = partition(grid)
    x5 = fork(multiply, height, width)
    x6 = fork(equality, size, x5)
    x7 = extract(x4, x6)
    x8 = color(x7)
    x9 = palette(grid)
    x10 = remove(x3, x9)
    x11 = other(x10, x8)
    x12 = ofcolor(grid, x11)
    x13 = vmirror(x12)
    x14 = hmirror(x12)
    x15 = toindices(x7)
    x16 = combine(x15, x12)
    x17 = height(x16)
    x18 = halve(x17)
    x19 = increment(x18)
    x20 = width(x16)
    x21 = halve(x20)
    x22 = increment(x21)
    x23 = astuple(x19, x22)
    x24 = maximum(x23)
    x25 = invert(x24)
    x26 = increment(x24)
    x27 = interval(x25, x26, ONE)
    x28 = product(x27, x27)
    x29 = initset(x14)
    x30 = insert(x13, x29)
    x31 = product(x28, x30)
    x32 = ofcolor(grid, x3)
    x33 = rbind(intersection, x32)
    x34 = fork(shift, last, first)
    x35 = chain(size, x33, x34)
    x36 = matcher(x35, ZERO)
    x37 = sfilter(x31, x36)
    x38 = rbind(intersection, x12)
    x39 = fork(shift, last, first)
    x40 = chain(size, x38, x39)
    x41 = argmax(x37, x40)
    x42 = first(x41)
    x43 = last(x41)
    x44 = fill(grid, x3, x7)
    x45 = shift(x43, x42)
    x46 = fill(x44, x11, x45)
    return x46


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
