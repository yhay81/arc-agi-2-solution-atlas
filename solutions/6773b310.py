"""Executable re-arc DSL program for ARC-AGI-2 task 6773b310.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    F,
    T,
    apply,
    argmin,
    astuple,
    canvas,
    color,
    colorcount,
    divide,
    fill,
    first,
    frontiers,
    hconcat,
    hline,
    increment,
    lbind,
    matcher,
    merge,
    objects,
    other,
    palette,
    rbind,
    remove,
    sfilter,
    shape,
    size,
    ulcorner,
    valmax,
    vline,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "6773b310"
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
    x6 = palette(grid)
    x7 = remove(x2, x6)
    x8 = lbind(colorcount, grid)
    x9 = argmin(x7, x8)
    x10 = other(x7, x9)
    x11 = objects(x5, F, T, T)
    x12 = rbind(colorcount, x9)
    x13 = valmax(x11, x12)
    x14 = rbind(colorcount, x9)
    x15 = matcher(x14, x13)
    x16 = sfilter(x11, x15)
    x17 = apply(ulcorner, x16)
    x18 = first(x11)
    x19 = shape(x18)
    x20 = increment(x19)
    x21 = rbind(divide, x20)
    x22 = apply(x21, x17)
    x23 = sfilter(x0, hline)
    x24 = size(x23)
    x25 = sfilter(x0, vline)
    x26 = size(x25)
    x27 = astuple(x24, x26)
    x28 = increment(x27)
    x29 = canvas(x10, x28)
    x30 = fill(x29, ONE, x22)
    return x30


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
