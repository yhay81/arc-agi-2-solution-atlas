"""Executable re-arc DSL program for ARC-AGI-2 task 75b8110e.

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

TASK_ID = "75b8110e"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = tophalf(grid)
    x1 = lefthalf(x0)
    x2 = tophalf(grid)
    x3 = righthalf(x2)
    x4 = bottomhalf(grid)
    x5 = righthalf(x4)
    x6 = bottomhalf(grid)
    x7 = lefthalf(x6)
    x8 = palette(x1)
    x9 = palette(x3)
    x10 = intersection(x8, x9)
    x11 = palette(x5)
    x12 = palette(x7)
    x13 = intersection(x11, x12)
    x14 = intersection(x10, x13)
    x15 = first(x14)
    x16 = shape(x1)
    x17 = canvas(x15, x16)
    x18 = matcher(first, x15)
    x19 = compose(flip, x18)
    x20 = rbind(sfilter, x19)
    x21 = compose(x20, asobject)
    x22 = x21(x1)
    x23 = x21(x5)
    x24 = x21(x7)
    x25 = x21(x3)
    x26 = paint(x17, x22)
    x27 = paint(x26, x23)
    x28 = paint(x27, x24)
    x29 = paint(x28, x25)
    return x29


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
