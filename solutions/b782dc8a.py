"""Executable re-arc DSL program for ARC-AGI-2 task b782dc8a.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    F,
    T,
    adjacent,
    argmin,
    chain,
    colorcount,
    colorfilter,
    combine,
    difference,
    even,
    fill,
    first,
    initset,
    lbind,
    leastcolor,
    manhattan,
    mapply,
    mfilter,
    neighbors,
    objects,
    ofcolor,
    palette,
    rbind,
    remove,
    sfilter,
    toindices,
    toobject,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "b782dc8a"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = palette(grid)
    x2 = remove(x0, x1)
    x3 = lbind(colorcount, grid)
    x4 = argmin(x2, x3)
    x5 = ofcolor(grid, x0)
    x6 = ofcolor(grid, x4)
    x7 = combine(x5, x6)
    x8 = mapply(neighbors, x7)
    x9 = difference(x8, x7)
    x10 = toobject(x9, grid)
    x11 = leastcolor(x10)
    x12 = ofcolor(grid, x0)
    x13 = first(x12)
    x14 = initset(x13)
    x15 = objects(grid, T, F, F)
    x16 = colorfilter(x15, x11)
    x17 = lbind(adjacent, x7)
    x18 = mfilter(x16, x17)
    x19 = toindices(x18)
    x20 = rbind(manhattan, x14)
    x21 = chain(even, x20, initset)
    x22 = sfilter(x19, x21)
    x23 = fill(grid, x4, x19)
    x24 = fill(x23, x0, x22)
    return x24


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
