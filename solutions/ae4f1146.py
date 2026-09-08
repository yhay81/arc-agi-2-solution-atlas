"""Executable re-arc DSL program for ARC-AGI-2 task ae4f1146.

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
    argmax,
    asindices,
    box,
    colorcount,
    mostcolor,
    objects,
    rbind,
    subgrid,
    toobject,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "ae4f1146"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asindices(grid)
    x1 = box(x0)
    x2 = toobject(x1, grid)
    mostcolor(x2)
    x4 = objects(grid, F, F, T)
    x5 = rbind(colorcount, ONE)
    x6 = argmax(x4, x5)
    x7 = subgrid(x6, grid)
    return x7


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
