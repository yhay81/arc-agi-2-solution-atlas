"""Executable re-arc DSL program for ARC-AGI-2 task 5117e062.

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
    fill,
    mostcolor,
    normalize,
    numcolors,
    objects,
    shape,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "5117e062"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, T, T)
    x1 = argmax(x0, numcolors)
    x2 = mostcolor(x1)
    x3 = normalize(x1)
    x4 = mostcolor(grid)
    x5 = shape(x1)
    x6 = canvas(x4, x5)
    x7 = fill(x6, x2, x3)
    return x7


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
