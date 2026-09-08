"""Executable re-arc DSL program for ARC-AGI-2 task 941d9a10.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    THREE,
    TWO,
    F,
    T,
    add,
    argmax,
    argmin,
    asindices,
    both,
    chain,
    colorfilter,
    compose,
    corners,
    equality,
    extract,
    fill,
    fork,
    greater,
    lbind,
    leftmost,
    mostcolor,
    objects,
    rbind,
    sfilter,
    size,
    toobject,
    uppermost,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "941d9a10"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asindices(grid)
    x1 = corners(x0)
    x2 = toobject(x1, grid)
    x3 = mostcolor(x2)
    x4 = objects(grid, T, T, F)
    x5 = colorfilter(x4, x3)
    x6 = fork(add, leftmost, uppermost)
    x7 = argmin(x5, x6)
    x8 = argmax(x5, x6)
    x9 = lbind(sfilter, x5)
    x10 = rbind(compose, leftmost)
    x11 = chain(size, x9, x10)
    x12 = lbind(sfilter, x5)
    x13 = rbind(compose, uppermost)
    x14 = chain(size, x12, x13)
    x15 = lbind(lbind, greater)
    x16 = chain(x11, x15, leftmost)
    x17 = lbind(rbind, greater)
    x18 = chain(x11, x17, leftmost)
    x19 = lbind(lbind, greater)
    x20 = chain(x14, x19, uppermost)
    x21 = lbind(rbind, greater)
    x22 = chain(x14, x21, uppermost)
    x23 = fork(equality, x16, x18)
    x24 = fork(equality, x20, x22)
    x25 = fork(both, x23, x24)
    x26 = extract(x5, x25)
    x27 = fill(grid, ONE, x7)
    x28 = fill(x27, THREE, x8)
    x29 = fill(x28, TWO, x26)
    return x29


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
