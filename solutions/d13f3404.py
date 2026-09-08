"""Executable re-arc DSL program for ARC-AGI-2 task d13f3404.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    UNITY,
    apply,
    asobject,
    canvas,
    center,
    color,
    compose,
    double,
    first,
    flip,
    fork,
    initset,
    mapply,
    matcher,
    mostcolor,
    paint,
    rbind,
    recolor,
    sfilter,
    shape,
    shoot,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d13f3404"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asobject(grid)
    x1 = mostcolor(grid)
    x2 = matcher(first, x1)
    x3 = compose(flip, x2)
    x4 = sfilter(x0, x3)
    x5 = apply(initset, x4)
    x6 = rbind(shoot, UNITY)
    x7 = compose(x6, center)
    x8 = fork(recolor, color, x7)
    x9 = mapply(x8, x5)
    x10 = shape(grid)
    x11 = double(x10)
    x12 = mostcolor(grid)
    x13 = canvas(x12, x11)
    x14 = paint(x13, x9)
    return x14


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
