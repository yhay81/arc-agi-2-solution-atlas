"""Executable re-arc DSL program for ARC-AGI-2 task a68b268e.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.re_arc_dsl import (
    asobject,
    bottomhalf,
    canvas,
    compose,
    first,
    flip,
    halve,
    intersection,
    lefthalf,
    matcher,
    paint,
    palette,
    rbind,
    righthalf,
    sfilter,
    shape,
    tophalf,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "a68b268e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = tophalf(grid)
    x1 = lefthalf(x0)
    x2 = tophalf(grid)
    x3 = righthalf(x2)
    x4 = bottomhalf(grid)
    x5 = lefthalf(x4)
    x6 = bottomhalf(grid)
    x7 = righthalf(x6)
    x8 = palette(x1)
    x9 = palette(x3)
    x10 = intersection(x8, x9)
    x11 = palette(x5)
    x12 = palette(x7)
    x13 = intersection(x11, x12)
    x14 = intersection(x10, x13)
    x15 = first(x14)
    x16 = shape(grid)
    x17 = halve(x16)
    x18 = canvas(x15, x17)
    x19 = matcher(first, x15)
    x20 = compose(flip, x19)
    x21 = rbind(sfilter, x20)
    x22 = compose(x21, asobject)
    x23 = x22(x1)
    x24 = x22(x3)
    x25 = x22(x5)
    x26 = x22(x7)
    x27 = paint(x18, x26)
    x28 = paint(x27, x25)
    x29 = paint(x28, x24)
    x30 = paint(x29, x23)
    return x30


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
