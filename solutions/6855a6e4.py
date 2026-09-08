"""Executable re-arc DSL program for ARC-AGI-2 task 6855a6e4.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    TWO,
    ZERO,
    add,
    argmin,
    both,
    box,
    branch,
    center,
    chain,
    color,
    colorcount,
    combine,
    compose,
    difference,
    dmirror,
    double,
    either,
    equality,
    extract,
    fill,
    fork,
    greater,
    height,
    identity,
    intersection,
    invert,
    last,
    lbind,
    leftmost,
    matcher,
    ofcolor,
    other,
    palette,
    partition,
    positive,
    rbind,
    remove,
    rightmost,
    sfilter,
    shift,
    size,
    subtract,
    toindices,
    tojvec,
    vfrontier,
    vmirror,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "6855a6e4"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = fork(difference, toindices, box)
    x2 = compose(size, x1)
    x3 = matcher(x2, ZERO)
    x4 = rbind(add, FOUR)
    x5 = chain(x4, double, width)
    x6 = fork(equality, size, x5)
    x7 = chain(x4, double, height)
    x8 = fork(equality, size, x7)
    x9 = fork(either, x6, x8)
    x10 = fork(both, x3, x9)
    x11 = extract(x0, x10)
    x12 = toindices(x11)
    x13 = center(x11)
    x14 = vfrontier(x13)
    x15 = intersection(x12, x14)
    x16 = size(x15)
    x17 = positive(x16)
    x18 = branch(x17, dmirror, identity)
    x19 = x18(grid)
    x20 = color(x11)
    x21 = palette(grid)
    x22 = remove(x20, x21)
    x23 = lbind(colorcount, grid)
    x24 = argmin(x22, x23)
    x25 = other(x22, x24)
    x26 = ofcolor(x19, x24)
    x27 = ofcolor(x19, x20)
    x28 = leftmost(x27)
    x29 = lbind(greater, x28)
    x30 = compose(x29, last)
    x31 = sfilter(x26, x30)
    x32 = difference(x26, x31)
    x33 = vmirror(x31)
    x34 = leftmost(x27)
    x35 = leftmost(x31)
    x36 = subtract(x34, x35)
    x37 = add(TWO, x36)
    x38 = tojvec(x37)
    x39 = shift(x33, x38)
    x40 = vmirror(x32)
    x41 = rightmost(x32)
    x42 = rightmost(x27)
    x43 = subtract(x41, x42)
    x44 = add(TWO, x43)
    x45 = tojvec(x44)
    x46 = invert(x45)
    x47 = shift(x40, x46)
    x48 = fill(x19, x25, x26)
    x49 = combine(x39, x47)
    x50 = fill(x48, x24, x49)
    x51 = x18(x50)
    return x51


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
