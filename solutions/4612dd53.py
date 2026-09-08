"""Executable re-arc DSL program for ARC-AGI-2 task 4612dd53.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    box,
    branch,
    fill,
    greater,
    hfrontier,
    leastcolor,
    mapply,
    ofcolor,
    shift,
    size,
    subgrid,
    ulcorner,
    underfill,
    vfrontier,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "4612dd53"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = leastcolor(grid)
    x1 = ofcolor(grid, x0)
    x2 = box(x1)
    x3 = fill(grid, TWO, x2)
    x4 = subgrid(x1, x3)
    x5 = ofcolor(x4, x0)
    x6 = mapply(vfrontier, x5)
    x7 = mapply(hfrontier, x5)
    x8 = size(x6)
    x9 = size(x7)
    x10 = greater(x8, x9)
    x11 = branch(x10, x7, x6)
    x12 = fill(x4, TWO, x11)
    x13 = ofcolor(x12, TWO)
    x14 = ulcorner(x1)
    x15 = shift(x13, x14)
    x16 = underfill(grid, TWO, x15)
    return x16


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
