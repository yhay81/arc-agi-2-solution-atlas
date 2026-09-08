"""Executable re-arc DSL program for ARC-AGI-2 task 3906de3d.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    TWO,
    ZERO,
    apply,
    argmin,
    branch,
    color,
    dedupe,
    dmirror,
    equality,
    extract,
    fill,
    first,
    greater,
    hmirror,
    identity,
    last,
    matcher,
    ofcolor,
    order,
    other,
    partition,
    rbind,
    remove,
    sfilter,
    size,
    uppermost,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "3906de3d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = first(grid)
    x1 = dedupe(x0)
    x2 = size(x1)
    x3 = equality(ONE, x2)
    x4 = branch(x3, dmirror, identity)
    x5 = x4(grid)
    x6 = first(x5)
    x7 = first(x6)
    x8 = first(x5)
    x9 = matcher(identity, x7)
    x10 = sfilter(x8, x9)
    x11 = size(x10)
    x12 = last(x5)
    x13 = sfilter(x12, x9)
    x14 = size(x13)
    x15 = greater(x11, x14)
    x16 = branch(x15, hmirror, identity)
    x17 = x16(x5)
    x18 = partition(x17)
    x19 = matcher(color, x7)
    x20 = extract(x18, x19)
    x21 = remove(x20, x18)
    x22 = argmin(x21, uppermost)
    x23 = other(x21, x22)
    x24 = color(x22)
    x25 = color(x23)
    x26 = fill(x17, TWO, x20)
    x27 = fill(x26, ONE, x23)
    x28 = fill(x27, ZERO, x22)
    x29 = rbind(order, identity)
    x30 = dmirror(x28)
    x31 = apply(x29, x30)
    x32 = dmirror(x31)
    x33 = x16(x32)
    x34 = x4(x33)
    x35 = ofcolor(x34, TWO)
    x36 = fill(x34, x7, x35)
    x37 = ofcolor(x34, ONE)
    x38 = fill(x36, x25, x37)
    x39 = ofcolor(x34, ZERO)
    x40 = fill(x38, x24, x39)
    return x40


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
