"""Executable re-arc DSL program for ARC-AGI-2 task 88a10436.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    F,
    T,
    apply,
    argmax,
    center,
    halve,
    invert,
    lbind,
    mapply,
    normalize,
    objects,
    paint,
    shape,
    shift,
    size,
    sizefilter,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "88a10436"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, F, T)
    x1 = argmax(x0, size)
    x2 = normalize(x1)
    x3 = shape(x1)
    x4 = halve(x3)
    x5 = invert(x4)
    x6 = shift(x2, x5)
    x7 = sizefilter(x0, ONE)
    x8 = apply(center, x7)
    x9 = lbind(shift, x6)
    x10 = mapply(x9, x8)
    x11 = paint(grid, x10)
    return x11


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
