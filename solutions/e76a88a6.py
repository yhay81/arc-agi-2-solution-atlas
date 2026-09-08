"""Executable re-arc DSL program for ARC-AGI-2 task e76a88a6.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    F,
    T,
    apply,
    argmax,
    lbind,
    mapply,
    normalize,
    numcolors,
    objects,
    paint,
    remove,
    shift,
    ulcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "e76a88a6"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, F, T)
    x1 = argmax(x0, numcolors)
    x2 = normalize(x1)
    x3 = remove(x1, x0)
    x4 = apply(ulcorner, x3)
    x5 = lbind(shift, x2)
    x6 = mapply(x5, x4)
    x7 = paint(grid, x6)
    return x7


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
