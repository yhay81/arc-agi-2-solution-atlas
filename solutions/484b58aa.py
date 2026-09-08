"""Executable re-arc DSL program for ARC-AGI-2 task 484b58aa.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ORIGIN,
    F,
    T,
    apply,
    argmin,
    asobject,
    astuple,
    colorcount,
    colorfilter,
    compose,
    contained,
    dmirror,
    first,
    flip,
    hperiod,
    lbind,
    mapply,
    matcher,
    multiply,
    neighbors,
    objects,
    paint,
    palette,
    sfilter,
    shift,
    size,
    valmin,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "484b58aa"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = palette(grid)
    x1 = objects(grid, T, F, F)
    x2 = lbind(colorfilter, x1)
    x3 = compose(size, x2)
    x4 = valmin(x0, x3)
    x5 = matcher(x3, x4)
    x6 = sfilter(x0, x5)
    x7 = lbind(colorcount, grid)
    x8 = argmin(x6, x7)
    x9 = asobject(grid)
    x10 = matcher(first, x8)
    x11 = compose(flip, x10)
    x12 = sfilter(x9, x11)
    x13 = lbind(contained, x8)
    x14 = compose(flip, x13)
    x15 = sfilter(grid, x14)
    x16 = asobject(x15)
    x17 = hperiod(x16)
    x18 = dmirror(grid)
    x19 = sfilter(x18, x14)
    x20 = asobject(x19)
    x21 = hperiod(x20)
    x22 = astuple(x21, x17)
    x23 = lbind(multiply, x22)
    x24 = neighbors(ORIGIN)
    x25 = mapply(neighbors, x24)
    x26 = apply(x23, x25)
    x27 = lbind(shift, x12)
    x28 = mapply(x27, x26)
    x29 = paint(grid, x28)
    return x29


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
