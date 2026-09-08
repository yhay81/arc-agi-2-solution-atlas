"""Executable re-arc DSL program for ARC-AGI-2 task 1190e5a7.

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
    astuple,
    canvas,
    corners,
    difference,
    equality,
    fill,
    frontiers,
    increment,
    mostcolor,
    ofcolor,
    palette,
    rbind,
    sfilter,
    size,
    toobject,
    vline,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "1190e5a7"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asindices(grid)
    x1 = corners(x0)
    x2 = toobject(x1, grid)
    x3 = mostcolor(x2)
    x4 = palette(grid)
    x5 = rbind(equality, x3)
    x6 = argmin(x4, x5)
    x7 = asindices(grid)
    x8 = ofcolor(grid, x3)
    x9 = difference(x7, x8)
    x10 = fill(grid, x6, x9)
    x11 = frontiers(x10)
    x12 = sfilter(x11, vline)
    x13 = difference(x11, x12)
    x14 = astuple(x13, x12)
    x15 = apply(size, x14)
    x16 = increment(x15)
    x17 = canvas(x3, x16)
    return x17


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
