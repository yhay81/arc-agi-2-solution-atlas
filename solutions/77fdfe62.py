"""Executable re-arc DSL program for ARC-AGI-2 task 77fdfe62.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ORIGIN,
    asindices,
    bottomhalf,
    box,
    color,
    compress,
    corners,
    decrement,
    difference,
    hconcat,
    height,
    index,
    lefthalf,
    other,
    palette,
    replace,
    righthalf,
    shape,
    toivec,
    tojvec,
    toobject,
    tophalf,
    trim,
    vconcat,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "77fdfe62"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = trim(grid)
    x1 = trim(x0)
    x2 = tophalf(x1)
    x3 = lefthalf(x2)
    x4 = tophalf(x1)
    x5 = righthalf(x4)
    x6 = bottomhalf(x1)
    x7 = lefthalf(x6)
    x8 = bottomhalf(x1)
    x9 = righthalf(x8)
    x10 = index(grid, ORIGIN)
    x11 = width(grid)
    x12 = decrement(x11)
    x13 = tojvec(x12)
    x14 = index(grid, x13)
    x15 = height(grid)
    x16 = decrement(x15)
    x17 = toivec(x16)
    x18 = index(grid, x17)
    x19 = shape(grid)
    x20 = decrement(x19)
    x21 = index(grid, x20)
    x22 = compress(grid)
    x23 = asindices(x22)
    x24 = box(x23)
    x25 = corners(x23)
    x26 = difference(x24, x25)
    x27 = toobject(x26, x22)
    x28 = color(x27)
    x29 = palette(x1)
    x30 = other(x29, x28)
    x31 = replace(x3, x30, x10)
    x32 = replace(x5, x30, x14)
    x33 = replace(x7, x30, x18)
    x34 = replace(x9, x30, x21)
    x35 = hconcat(x31, x32)
    x36 = hconcat(x33, x34)
    x37 = vconcat(x35, x36)
    return x37


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
