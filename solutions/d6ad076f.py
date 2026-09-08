"""Executable re-arc DSL program for ARC-AGI-2 task d6ad076f.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    adjacent,
    apply,
    astuple,
    backdrop,
    branch,
    combine,
    compose,
    contained,
    decrement,
    equality,
    extract,
    fill,
    first,
    flip,
    fork,
    hmatching,
    increment,
    initset,
    insert,
    last,
    leftmost,
    lowermost,
    maximum,
    merge,
    minimum,
    partition,
    product,
    rbind,
    rightmost,
    sfilter,
    toindices,
    totuple,
    uppermost,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d6ad076f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = product(x0, x0)
    x2 = fork(equality, first, last)
    x3 = compose(flip, x2)
    x4 = sfilter(x1, x3)
    x5 = fork(adjacent, first, last)
    x6 = compose(flip, x5)
    x7 = extract(x4, x6)
    x8 = totuple(x7)
    x9 = first(x8)
    x10 = last(x8)
    x11 = combine(x9, x10)
    x12 = leftmost(x11)
    x13 = increment(x12)
    x14 = rightmost(x11)
    x15 = decrement(x14)
    x16 = apply(uppermost, x8)
    x17 = maximum(x16)
    x18 = increment(x17)
    x19 = apply(lowermost, x8)
    x20 = minimum(x19)
    x21 = decrement(x20)
    x22 = apply(leftmost, x8)
    x23 = maximum(x22)
    x24 = increment(x23)
    x25 = apply(rightmost, x8)
    x26 = minimum(x25)
    x27 = decrement(x26)
    x28 = uppermost(x11)
    x29 = increment(x28)
    x30 = lowermost(x11)
    x31 = decrement(x30)
    x32 = hmatching(x9, x10)
    x33 = branch(x32, x13, x24)
    x34 = branch(x32, x15, x27)
    x35 = branch(x32, x21, x31)
    x36 = branch(x32, x18, x29)
    x37 = astuple(x35, x34)
    x38 = astuple(x36, x33)
    x39 = initset(x38)
    x40 = insert(x37, x39)
    x41 = backdrop(x40)
    x42 = merge(x7)
    x43 = toindices(x42)
    x44 = rbind(contained, x43)
    x45 = compose(flip, x44)
    x46 = sfilter(x41, x45)
    x47 = fill(grid, EIGHT, x46)
    return x47


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
