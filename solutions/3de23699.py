"""Executable re-arc DSL program for ARC-AGI-2 task 3de23699.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.re_arc_dsl import (
    asindices,
    combine,
    corners,
    dneighbors,
    first,
    identity,
    last,
    mapply,
    mostcolor,
    ofcolor,
    order,
    palette,
    remove,
    subgrid,
    switch,
    toobject,
    trim,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "3de23699"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = asindices(grid)
    x1 = corners(x0)
    x2 = mapply(dneighbors, x1)
    x3 = toobject(x2, grid)
    x4 = mostcolor(x3)
    x5 = palette(grid)
    x6 = remove(x4, x5)
    x7 = order(x6, identity)
    x8 = first(x7)
    x9 = last(x7)
    x10 = ofcolor(grid, x8)
    x11 = ofcolor(grid, x9)
    x12 = switch(grid, x9, x8)
    x13 = combine(x10, x11)
    x14 = subgrid(x13, x12)
    x15 = trim(x14)
    return x15


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
