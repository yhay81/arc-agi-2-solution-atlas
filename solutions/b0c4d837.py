"""Executable re-arc DSL program for ARC-AGI-2 task b0c4d837.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NINE,
    ONE,
    THREE,
    TWO,
    ZERO,
    argmax,
    argmin,
    branch,
    color,
    combine,
    connect,
    decrement,
    difference,
    equality,
    extract,
    first,
    fork,
    height,
    hsplit,
    interval,
    last,
    llcorner,
    lrcorner,
    matcher,
    multiply,
    pair,
    partition,
    remove,
    repeat,
    size,
    subtract,
    toindices,
    ulcorner,
    urcorner,
    vconcat,
    vmirror,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "b0c4d837"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = fork(multiply, height, width)
    x2 = argmax(x0, x1)
    x3 = remove(x2, x0)
    x4 = argmin(x3, x1)
    x5 = argmax(x3, x1)
    x6 = ulcorner(x5)
    x7 = llcorner(x5)
    x8 = connect(x6, x7)
    x9 = urcorner(x5)
    x10 = lrcorner(x5)
    x11 = connect(x9, x10)
    x12 = combine(x8, x11)
    x13 = toindices(x5)
    x14 = difference(x12, x13)
    x15 = size(x14)
    x16 = equality(x15, ZERO)
    x17 = branch(x16, height, width)
    x18 = x17(x5)
    x19 = x17(x4)
    x20 = subtract(x18, x19)
    x21 = decrement(x20)
    x22 = color(x4)
    x23 = color(x2)
    x24 = repeat(x22, x21)
    x25 = subtract(NINE, x21)
    x26 = repeat(x23, x25)
    x27 = combine(x24, x26)
    x28 = repeat(x27, ONE)
    x29 = hsplit(x28, THREE)
    x30 = interval(ZERO, THREE, ONE)
    x31 = pair(x30, x29)
    x32 = matcher(first, ZERO)
    x33 = extract(x31, x32)
    x34 = last(x33)
    x35 = matcher(first, ONE)
    x36 = extract(x31, x35)
    x37 = last(x36)
    x38 = matcher(first, TWO)
    x39 = extract(x31, x38)
    x40 = last(x39)
    x41 = vmirror(x37)
    x42 = vconcat(x34, x41)
    x43 = vconcat(x42, x40)
    return x43


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
