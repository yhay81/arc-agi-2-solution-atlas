"""Executable re-arc DSL program for ARC-AGI-2 task 7c008303.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    F,
    T,
    argmax,
    argmin,
    asindices,
    asobject,
    canvas,
    color,
    compose,
    contained,
    difference,
    frontiers,
    halve,
    hconcat,
    height,
    hupscale,
    last,
    merge,
    objects,
    ofcolor,
    paint,
    rbind,
    remove,
    sfilter,
    shape,
    size,
    subgrid,
    vupscale,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "7c008303"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = merge(x0)
    x2 = color(x1)
    x3 = shape(grid)
    x4 = canvas(x2, x3)
    x5 = hconcat(grid, x4)
    x6 = objects(x5, F, F, T)
    x7 = argmin(x6, size)
    x8 = argmax(x6, size)
    x9 = remove(x8, x6)
    x10 = remove(x7, x9)
    x11 = merge(x10)
    x12 = color(x11)
    x13 = subgrid(x8, grid)
    x14 = subgrid(x7, grid)
    x15 = width(x8)
    x16 = halve(x15)
    x17 = hupscale(x14, x16)
    x18 = height(x8)
    x19 = halve(x18)
    x20 = vupscale(x17, x19)
    x21 = asobject(x20)
    x22 = asindices(x13)
    x23 = ofcolor(x13, x12)
    x24 = difference(x22, x23)
    x25 = rbind(contained, x24)
    x26 = compose(x25, last)
    x27 = sfilter(x21, x26)
    x28 = paint(x13, x27)
    return x28


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
