"""Executable re-arc DSL program for ARC-AGI-2 task 4093f84a.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.re_arc_dsl import (
    apply,
    argmin,
    asindices,
    branch,
    colorcount,
    compose,
    dmirror,
    equality,
    fork,
    frontiers,
    greater,
    hconcat,
    height,
    identity,
    last,
    lbind,
    leftmost,
    merge,
    multiply,
    ofcolor,
    order,
    palette,
    positive,
    rbind,
    remove,
    replace,
    rightmost,
    sfilter,
    subgrid,
    vmirror,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "4093f84a"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = merge(x0)
    x2 = palette(x1)
    x3 = fork(multiply, height, width)
    x4 = lbind(ofcolor, grid)
    x5 = compose(x3, x4)
    x6 = argmin(x2, x5)
    x7 = palette(grid)
    x8 = remove(x6, x7)
    x9 = lbind(colorcount, grid)
    x10 = argmin(x8, x9)
    x11 = ofcolor(grid, x6)
    x12 = leftmost(x11)
    x13 = positive(x12)
    x14 = branch(x13, identity, dmirror)
    x15 = x14(grid)
    x16 = ofcolor(x15, x6)
    x17 = subgrid(x16, x15)
    x18 = leftmost(x16)
    x19 = rightmost(x16)
    x20 = lbind(greater, x18)
    x21 = compose(x20, last)
    x22 = rbind(greater, x19)
    x23 = compose(x22, last)
    x24 = asindices(x15)
    x25 = sfilter(x24, x21)
    x26 = subgrid(x25, x15)
    x27 = asindices(x15)
    x28 = sfilter(x27, x23)
    x29 = subgrid(x28, x15)
    x30 = rbind(equality, x10)
    x31 = rbind(order, x30)
    x32 = apply(x31, x26)
    x33 = vmirror(x29)
    x34 = apply(x31, x33)
    x35 = vmirror(x34)
    x36 = hconcat(x32, x17)
    x37 = hconcat(x36, x35)
    x38 = x14(x37)
    x39 = replace(x38, x10, x6)
    return x39


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
