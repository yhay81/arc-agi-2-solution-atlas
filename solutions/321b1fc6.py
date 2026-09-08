"""Executable re-arc DSL program for ARC-AGI-2 task 321b1fc6.

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
    cover,
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

TASK_ID = "321b1fc6"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, F, F, T)
    x1 = argmax(x0, numcolors)
    x2 = remove(x1, x0)
    x3 = normalize(x1)
    x4 = apply(ulcorner, x2)
    x5 = lbind(shift, x3)
    x6 = mapply(x5, x4)
    x7 = paint(grid, x6)
    x8 = cover(x7, x1)
    return x8


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
