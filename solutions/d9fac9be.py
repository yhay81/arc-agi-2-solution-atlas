"""Executable re-arc DSL program for ARC-AGI-2 task d9fac9be.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    UNITY,
    branch,
    canvas,
    combine,
    first,
    initset,
    last,
    mostcolor,
    neighbors,
    occurrences,
    palette,
    positive,
    recolor,
    remove,
    size,
    totuple,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d9fac9be"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = palette(grid)
    x2 = remove(x0, x1)
    x3 = totuple(x2)
    x4 = first(x3)
    x5 = last(x3)
    x6 = neighbors(UNITY)
    x7 = initset(UNITY)
    x8 = recolor(x4, x6)
    x9 = recolor(x5, x7)
    x10 = combine(x8, x9)
    x11 = occurrences(grid, x10)
    x12 = size(x11)
    x13 = positive(x12)
    x14 = branch(x13, x5, x4)
    x15 = canvas(x14, UNITY)
    return x15


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
