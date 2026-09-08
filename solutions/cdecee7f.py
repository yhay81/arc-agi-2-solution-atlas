"""Executable re-arc DSL program for ARC-AGI-2 task cdecee7f.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    DOWN,
    NINE,
    ONE,
    ORIGIN,
    THREE,
    TWO_BY_ZERO,
    UNITY,
    apply,
    asobject,
    astuple,
    canvas,
    color,
    compose,
    crop,
    dmirror,
    first,
    flip,
    hconcat,
    hsplit,
    initset,
    leftmost,
    matcher,
    merge,
    mostcolor,
    order,
    rbind,
    sfilter,
    size,
    subtract,
    vconcat,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "cdecee7f"
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
    x6 = astuple(ONE, THREE)
    x7 = size(x5)
    x8 = order(x5, leftmost)
    x9 = apply(color, x8)
    x10 = rbind(canvas, UNITY)
    x11 = apply(x10, x9)
    x12 = merge(x11)
    x13 = dmirror(x12)
    x14 = subtract(NINE, x7)
    x15 = astuple(ONE, x14)
    x16 = mostcolor(grid)
    x17 = canvas(x16, x15)
    x18 = hconcat(x13, x17)
    x19 = hsplit(x18, THREE)
    x20 = merge(x19)
    x21 = crop(x20, ORIGIN, x6)
    x22 = crop(x20, DOWN, x6)
    x23 = crop(x20, TWO_BY_ZERO, x6)
    x24 = vmirror(x22)
    x25 = vconcat(x21, x24)
    x26 = vconcat(x25, x23)
    return x26


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
