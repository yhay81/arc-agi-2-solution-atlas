"""Executable re-arc DSL program for ARC-AGI-2 task 7ddcd7ec.

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
    center,
    color,
    fork,
    lbind,
    mapply,
    objects,
    paint,
    position,
    recolor,
    remove,
    shoot,
    size,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "7ddcd7ec"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, F, T)
    x1 = argmax(x0, size)
    x2 = remove(x1, x0)
    x3 = lbind(position, x1)
    x4 = fork(shoot, center, x3)
    x5 = fork(recolor, color, x4)
    x6 = mapply(x5, x2)
    x7 = paint(grid, x6)
    return x7


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
