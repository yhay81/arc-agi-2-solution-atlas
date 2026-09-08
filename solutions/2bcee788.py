"""Executable re-arc DSL program for ARC-AGI-2 task 2bcee788.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    THREE,
    argmax,
    argmin,
    branch,
    decrement,
    double,
    fill,
    fork,
    greater,
    height,
    hmatching,
    hmirror,
    leftmost,
    multiply,
    paint,
    partition,
    remove,
    shape,
    shift,
    size,
    toivec,
    tojvec,
    uppermost,
    vmirror,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "2bcee788"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = fork(multiply, height, width)
    x2 = argmax(x0, x1)
    x3 = remove(x2, x0)
    x4 = argmin(x3, size)
    x5 = argmax(x3, size)
    x6 = hmatching(x4, x5)
    x7 = branch(x6, vmirror, hmirror)
    x8 = x7(x5)
    x9 = branch(x6, leftmost, uppermost)
    x10 = branch(x6, tojvec, toivec)
    x11 = x9(x4)
    x12 = x9(x5)
    x13 = greater(x11, x12)
    x14 = double(x13)
    x15 = decrement(x14)
    x16 = x10(x15)
    x17 = shape(x5)
    x18 = multiply(x16, x17)
    x19 = shift(x8, x18)
    x20 = fill(grid, THREE, x2)
    x21 = paint(x20, x19)
    return x21


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
