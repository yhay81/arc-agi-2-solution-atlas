"""Executable re-arc DSL program for ARC-AGI-2 task c444b776.

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
    canvas,
    frontiers,
    hconcat,
    lbind,
    leastcolor,
    mapply,
    merge,
    normalize,
    numcolors,
    objects,
    paint,
    shape,
    shift,
    ulcorner,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "c444b776"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = frontiers(grid)
    x1 = merge(x0)
    x2 = leastcolor(x1)
    x3 = shape(grid)
    x4 = canvas(x2, x3)
    x5 = hconcat(grid, x4)
    x6 = objects(x5, F, F, T)
    x7 = argmax(x6, numcolors)
    x8 = apply(ulcorner, x6)
    x9 = normalize(x7)
    x10 = lbind(shift, x9)
    x11 = mapply(x10, x8)
    x12 = paint(grid, x11)
    return x12


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
