"""Executable re-arc DSL program for ARC-AGI-2 task 6b9890af.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    UNITY,
    T,
    argmax,
    asobject,
    box,
    difference,
    divide,
    equality,
    fgpartition,
    fork,
    height,
    hupscale,
    merge,
    multiply,
    objects,
    paint,
    sfilter,
    shift,
    subgrid,
    subtract,
    toindices,
    vupscale,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "6b9890af"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, T, T)
    x1 = fork(equality, toindices, box)
    x2 = sfilter(x0, x1)
    x3 = fork(multiply, height, width)
    x4 = argmax(x2, x3)
    x5 = fgpartition(grid)
    x6 = merge(x5)
    x7 = difference(x6, x4)
    x8 = subgrid(x4, grid)
    x9 = subgrid(x7, grid)
    x10 = height(x8)
    x11 = subtract(x10, TWO)
    x12 = height(x9)
    x13 = divide(x11, x12)
    x14 = width(x8)
    x15 = subtract(x14, TWO)
    x16 = width(x9)
    x17 = divide(x15, x16)
    x18 = hupscale(x9, x17)
    x19 = vupscale(x18, x13)
    x20 = asobject(x19)
    x21 = shift(x20, UNITY)
    x22 = paint(x8, x21)
    return x22


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
