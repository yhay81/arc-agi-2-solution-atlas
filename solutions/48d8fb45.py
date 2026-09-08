"""Executable re-arc DSL program for ARC-AGI-2 task 48d8fb45.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    F,
    T,
    argmax,
    canvas,
    first,
    matcher,
    mostcolor,
    normalize,
    numcolors,
    objects,
    paint,
    sfilter,
    shape,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "48d8fb45"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, T, T)
    x1 = argmax(x0, numcolors)
    x2 = mostcolor(x1)
    x3 = matcher(first, x2)
    x4 = sfilter(x1, x3)
    x5 = shape(x4)
    x6 = normalize(x4)
    x7 = mostcolor(grid)
    x8 = canvas(x7, x5)
    x9 = paint(x8, x6)
    return x9


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
