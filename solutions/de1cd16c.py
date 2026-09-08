"""Executable re-arc DSL program for ARC-AGI-2 task de1cd16c.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    UNITY,
    F,
    T,
    apply,
    argmax,
    branch,
    canvas,
    chain,
    color,
    colorcount,
    colorfilter,
    compose,
    dedupe,
    difference,
    equality,
    lbind,
    leastcolor,
    merge,
    mostcolor,
    mostcommon,
    objects,
    rbind,
    size,
    subgrid,
    totuple,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "de1cd16c"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = totuple(x0)
    x2 = apply(color, x1)
    x3 = size(x2)
    x4 = dedupe(x2)
    x5 = size(x4)
    x6 = equality(x3, x5)
    x7 = compose(leastcolor, merge)
    x8 = lbind(apply, color)
    x9 = chain(mostcommon, x8, totuple)
    x10 = branch(x6, x7, x9)
    x11 = x10(x0)
    x12 = objects(grid, T, F, F)
    x13 = colorfilter(x12, x11)
    x14 = difference(x12, x13)
    x15 = rbind(subgrid, grid)
    x16 = apply(x15, x14)
    x17 = rbind(colorcount, x11)
    x18 = argmax(x16, x17)
    x19 = mostcolor(x18)
    x20 = canvas(x19, UNITY)
    return x20


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
