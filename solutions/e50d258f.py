"""Executable re-arc DSL program for ARC-AGI-2 task e50d258f.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    F,
    T,
    argmax,
    asindices,
    box,
    canvas,
    colorcount,
    hconcat,
    mostcolor,
    objects,
    rbind,
    shape,
    subgrid,
    toobject,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "e50d258f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asindices(grid)
    x1 = box(x0)
    x2 = toobject(x1, grid)
    x3 = mostcolor(x2)
    x4 = shape(grid)
    x5 = canvas(x3, x4)
    x6 = hconcat(grid, x5)
    x7 = objects(x6, F, F, T)
    x8 = rbind(colorcount, TWO)
    x9 = argmax(x7, x8)
    x10 = subgrid(x9, grid)
    return x10


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
