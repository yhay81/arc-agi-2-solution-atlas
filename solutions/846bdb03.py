"""Executable re-arc DSL program for ARC-AGI-2 task 846bdb03.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    UNITY,
    backdrop,
    branch,
    color,
    corners,
    cover,
    dmirror,
    equality,
    extract,
    fgpartition,
    first,
    fork,
    frontiers,
    greater,
    hline,
    identity,
    last,
    leftmost,
    merge,
    mostcolor,
    normalize,
    ofcolor,
    paint,
    palette,
    partition,
    positive,
    remove,
    sfilter,
    shift,
    size,
    subgrid,
    toindices,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "846bdb03"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = fork(equality, corners, toindices)
    x2 = extract(x0, x1)
    x3 = subgrid(x2, grid)
    x4 = backdrop(x2)
    x5 = cover(grid, x4)
    x6 = frontiers(x3)
    x7 = sfilter(x6, hline)
    x8 = size(x7)
    x9 = positive(x8)
    x10 = branch(x9, dmirror, identity)
    x11 = x10(x3)
    x12 = x10(x5)
    x13 = fgpartition(x12)
    x14 = merge(x13)
    x15 = normalize(x14)
    x16 = mostcolor(x12)
    x17 = color(x2)
    x18 = palette(x11)
    x19 = remove(x17, x18)
    x20 = remove(x16, x19)
    x21 = first(x20)
    x22 = last(x20)
    x23 = ofcolor(x11, x22)
    x24 = leftmost(x23)
    x25 = ofcolor(x11, x21)
    x26 = leftmost(x25)
    x27 = greater(x24, x26)
    x28 = ofcolor(x12, x22)
    x29 = leftmost(x28)
    x30 = ofcolor(x12, x21)
    x31 = leftmost(x30)
    x32 = greater(x29, x31)
    x33 = equality(x27, x32)
    x34 = branch(x33, identity, vmirror)
    x35 = x34(x15)
    x36 = shift(x35, UNITY)
    x37 = paint(x11, x36)
    x38 = x10(x37)
    return x38


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
