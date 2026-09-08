"""Executable re-arc DSL program for ARC-AGI-2 task ff28f65a.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    NINE,
    ONE,
    THREE,
    TWO,
    ZERO,
    F,
    T,
    apply,
    argmax,
    astuple,
    canvas,
    colorcount,
    colorfilter,
    double,
    fill,
    hconcat,
    hsplit,
    interval,
    lbind,
    merge,
    objects,
    palette,
    remove,
    shape,
    size,
    tojvec,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "ff28f65a"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = palette(grid)
    x1 = remove(TWO, x0)
    x2 = lbind(colorcount, grid)
    x3 = argmax(x1, x2)
    x4 = shape(grid)
    x5 = canvas(x3, x4)
    x6 = hconcat(grid, x5)
    x7 = objects(x6, T, F, T)
    x8 = colorfilter(x7, TWO)
    x9 = size(x8)
    x10 = double(x9)
    x11 = interval(ZERO, x10, TWO)
    x12 = apply(tojvec, x11)
    x13 = astuple(ONE, NINE)
    x14 = canvas(x3, x13)
    x15 = fill(x14, ONE, x12)
    x16 = hsplit(x15, THREE)
    x17 = merge(x16)
    return x17


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
