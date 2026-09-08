"""Executable re-arc DSL program for ARC-AGI-2 task 39a8645d.

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
    T,
    apply,
    canvas,
    mostcolor,
    mostcommon,
    normalize,
    objects,
    paint,
    shape,
    totuple,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "39a8645d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, T, T)
    x1 = totuple(x0)
    x2 = apply(normalize, x1)
    x3 = mostcommon(x2)
    x4 = mostcolor(grid)
    x5 = shape(x3)
    x6 = canvas(x4, x5)
    x7 = paint(x6, x3)
    return x7


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
