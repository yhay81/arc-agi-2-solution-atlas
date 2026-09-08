"""Executable re-arc DSL program for ARC-AGI-2 task 760b3cac.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    FIVE,
    FOUR,
    LEFT,
    ONE,
    RIGHT,
    THREE_BY_THREE,
    TWO,
    UP,
    add,
    both,
    box,
    branch,
    compose,
    corners,
    either,
    equality,
    extract,
    fgpartition,
    first,
    fork,
    hmirror,
    intersection,
    last,
    leftmost,
    lowermost,
    matcher,
    multiply,
    other,
    paint,
    rightmost,
    sfilter,
    shape,
    shift,
    size,
    toindices,
    uppermost,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "760b3cac"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = matcher(shape, THREE_BY_THREE)
    x2 = matcher(size, FIVE)
    x3 = fork(intersection, toindices, box)
    x4 = compose(size, x3)
    x5 = matcher(x4, FOUR)
    x6 = fork(intersection, toindices, corners)
    x7 = compose(size, x6)
    x8 = matcher(x7, ONE)
    x9 = fork(both, x1, x2)
    x10 = fork(both, x5, x8)
    x11 = fork(both, x9, x10)
    x12 = extract(x0, x11)
    x13 = toindices(x12)
    x14 = lowermost(x12)
    x15 = matcher(first, x14)
    x16 = uppermost(x12)
    x17 = matcher(first, x16)
    x18 = rightmost(x12)
    x19 = matcher(last, x18)
    x20 = leftmost(x12)
    x21 = matcher(last, x20)
    x22 = sfilter(x13, x15)
    x23 = size(x22)
    x24 = equality(x23, TWO)
    x25 = sfilter(x13, x17)
    x26 = size(x25)
    x27 = equality(x26, TWO)
    x28 = sfilter(x13, x19)
    x29 = size(x28)
    x30 = equality(x29, TWO)
    x31 = sfilter(x13, x21)
    x32 = size(x31)
    x33 = equality(x32, TWO)
    x34 = either(x24, x27)
    x35 = branch(x34, hmirror, vmirror)
    x36 = multiply(x24, DOWN)
    x37 = multiply(x27, UP)
    x38 = add(x36, x37)
    x39 = multiply(x30, RIGHT)
    x40 = multiply(x33, LEFT)
    x41 = add(x39, x40)
    x42 = add(x38, x41)
    x43 = other(x0, x12)
    x44 = x35(x43)
    x45 = shape(x43)
    x46 = multiply(x45, x42)
    x47 = shift(x44, x46)
    x48 = paint(grid, x47)
    return x48


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
