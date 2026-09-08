"""Executable re-arc DSL program for ARC-AGI-2 task 09629e4f.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    F,
    T,
    argmin,
    astuple,
    canvas,
    chain,
    color,
    first,
    fork,
    frontiers,
    hconcat,
    hline,
    increment,
    last,
    lbind,
    mapply,
    merge,
    multiply,
    normalize,
    numcolors,
    objects,
    paint,
    rbind,
    recolor,
    sfilter,
    shape,
    shift,
    size,
    toindices,
    vline,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "09629e4f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = sfilter(x0, hline)
    x2 = sfilter(x0, vline)
    x3 = size(x1)
    x4 = size(x2)
    x5 = merge(x0)
    x6 = color(x5)
    x7 = shape(grid)
    x8 = canvas(x6, x7)
    x9 = hconcat(grid, x8)
    x10 = objects(x9, F, T, T)
    x11 = argmin(x10, numcolors)
    x12 = normalize(x11)
    x13 = toindices(x12)
    x14 = increment(x3)
    x15 = increment(x14)
    x16 = increment(x4)
    x17 = increment(x16)
    x18 = astuple(x15, x17)
    x19 = lbind(shift, x13)
    x20 = rbind(multiply, x18)
    x21 = chain(x19, x20, last)
    x22 = fork(recolor, first, x21)
    x23 = normalize(x11)
    x24 = mapply(x22, x23)
    x25 = paint(x8, x24)
    return x25


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
