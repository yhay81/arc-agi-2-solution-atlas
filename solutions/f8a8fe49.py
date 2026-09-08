"""Executable re-arc DSL program for ARC-AGI-2 task f8a8fe49.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    UNITY,
    add,
    argmax,
    argmin,
    asobject,
    backdrop,
    branch,
    color,
    combine,
    dmirror,
    fill,
    fork,
    frontiers,
    height,
    hline,
    identity,
    inbox,
    invert,
    lefthalf,
    multiply,
    ofcolor,
    other,
    paint,
    partition,
    positive,
    remove,
    righthalf,
    sfilter,
    shift,
    size,
    subgrid,
    tojvec,
    trim,
    ulcorner,
    urcorner,
    vmirror,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "f8a8fe49"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = fork(multiply, height, width)
    x2 = argmin(x0, x1)
    x3 = argmax(x0, x1)
    x4 = remove(x2, x0)
    x5 = other(x4, x3)
    x6 = subgrid(x5, grid)
    x7 = frontiers(x6)
    x8 = sfilter(x7, hline)
    x9 = size(x8)
    x10 = positive(x9)
    x11 = branch(x10, dmirror, identity)
    x12 = x11(grid)
    x13 = color(x5)
    x14 = ofcolor(x12, x13)
    x15 = subgrid(x14, x12)
    x16 = trim(x15)
    x17 = lefthalf(x16)
    x18 = vmirror(x17)
    x19 = asobject(x18)
    x20 = righthalf(x16)
    x21 = vmirror(x20)
    x22 = asobject(x21)
    x23 = color(x3)
    x24 = inbox(x14)
    x25 = backdrop(x24)
    x26 = fill(x12, x23, x25)
    x27 = urcorner(x14)
    x28 = add(x27, UNITY)
    x29 = shift(x22, x28)
    x30 = ulcorner(x14)
    x31 = width(x19)
    x32 = invert(x31)
    x33 = tojvec(x32)
    x34 = add(DOWN, x33)
    x35 = add(x30, x34)
    x36 = shift(x19, x35)
    x37 = combine(x29, x36)
    x38 = paint(x26, x37)
    x39 = x11(x38)
    return x39


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
