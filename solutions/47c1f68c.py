"""Executable re-arc DSL program for ARC-AGI-2 task 47c1f68c.

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
    argmax,
    asindices,
    astuple,
    bottomhalf,
    color,
    combine,
    compress,
    difference,
    fill,
    frontiers,
    hconcat,
    hmirror,
    lefthalf,
    merge,
    mostcolor,
    numcolors,
    ofcolor,
    righthalf,
    tophalf,
    vconcat,
    vmirror,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "47c1f68c"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = merge(x0)
    x2 = color(x1)
    x3 = compress(grid)
    x4 = mostcolor(x3)
    x5 = tophalf(grid)
    x6 = lefthalf(x5)
    x7 = vmirror(x6)
    x8 = hconcat(x6, x7)
    x9 = hmirror(x8)
    x10 = vconcat(x8, x9)
    x11 = tophalf(grid)
    x12 = righthalf(x11)
    x13 = vmirror(x12)
    x14 = hconcat(x13, x12)
    x15 = hmirror(x14)
    x16 = vconcat(x14, x15)
    x17 = bottomhalf(grid)
    x18 = lefthalf(x17)
    x19 = vmirror(x18)
    x20 = hconcat(x18, x19)
    x21 = hmirror(x20)
    x22 = vconcat(x21, x20)
    x23 = bottomhalf(grid)
    x24 = righthalf(x23)
    x25 = vmirror(x24)
    x26 = hconcat(x25, x24)
    x27 = hmirror(x26)
    x28 = vconcat(x27, x26)
    x29 = astuple(x10, x16)
    x30 = astuple(x22, x28)
    x31 = combine(x29, x30)
    x32 = argmax(x31, numcolors)
    x33 = asindices(x32)
    x34 = ofcolor(x32, x4)
    x35 = difference(x33, x34)
    x36 = fill(x32, x2, x35)
    return x36


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
