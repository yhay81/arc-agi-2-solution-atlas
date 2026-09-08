"""Executable re-arc DSL program for ARC-AGI-2 task 1c786137.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    SEVEN,
    F,
    T,
    box,
    color,
    colorfilter,
    compose,
    contained,
    equality,
    extract,
    fork,
    greater,
    lbind,
    matcher,
    objects,
    palette,
    rbind,
    sfilter,
    size,
    subgrid,
    toindices,
    trim,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "1c786137"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = lbind(colorfilter, x0)
    x2 = compose(size, x1)
    x3 = matcher(x2, ONE)
    x4 = palette(grid)
    x5 = sfilter(x4, x3)
    x6 = fork(equality, toindices, box)
    x7 = rbind(contained, x5)
    x8 = compose(x7, color)
    x9 = sfilter(x0, x8)
    x10 = rbind(greater, SEVEN)
    x11 = compose(x10, size)
    x12 = sfilter(x9, x11)
    x13 = extract(x12, x6)
    x14 = subgrid(x13, grid)
    x15 = trim(x14)
    return x15


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
