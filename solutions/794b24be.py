"""Executable re-arc DSL program for ARC-AGI-2 task 794b24be.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    ONE,
    ORIGIN,
    THREE_BY_THREE,
    TWO,
    UNITY,
    argmax,
    branch,
    canvas,
    colorcount,
    connect,
    decrement,
    equality,
    fill,
    initset,
    lbind,
    palette,
    remove,
    tojvec,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "794b24be"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = palette(grid)
    x1 = remove(ONE, x0)
    x2 = lbind(colorcount, grid)
    x3 = argmax(x1, x2)
    x4 = canvas(x3, THREE_BY_THREE)
    x5 = colorcount(grid, ONE)
    x6 = decrement(x5)
    x7 = tojvec(x6)
    x8 = connect(ORIGIN, x7)
    x9 = fill(x4, TWO, x8)
    x10 = initset(UNITY)
    x11 = equality(x5, FOUR)
    x12 = branch(x11, x10, x8)
    x13 = fill(x9, TWO, x12)
    return x13


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
