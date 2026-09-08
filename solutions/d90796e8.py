"""Executable re-arc DSL program for ARC-AGI-2 task d90796e8.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    THREE,
    TWO,
    chain,
    compose,
    cover,
    dneighbors,
    fill,
    intersection,
    lbind,
    ofcolor,
    positive,
    sfilter,
    size,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d90796e8"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = ofcolor(grid, TWO)
    x1 = ofcolor(grid, THREE)
    x2 = compose(positive, size)
    x3 = lbind(intersection, x1)
    x4 = chain(x2, x3, dneighbors)
    x5 = compose(positive, size)
    x6 = lbind(intersection, x0)
    x7 = chain(x5, x6, dneighbors)
    x8 = sfilter(x0, x4)
    x9 = sfilter(x1, x7)
    x10 = cover(grid, x8)
    x11 = fill(x10, EIGHT, x9)
    return x11


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
