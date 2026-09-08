"""Executable re-arc DSL program for ARC-AGI-2 task aedd82e4.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    ZERO,
    F,
    T,
    canvas,
    color,
    compose,
    fill,
    flip,
    hconcat,
    matcher,
    merge,
    objects,
    sfilter,
    shape,
    sizefilter,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "aedd82e4"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = shape(grid)
    x1 = canvas(ZERO, x0)
    x2 = hconcat(grid, x1)
    x3 = objects(x2, F, F, T)
    x4 = matcher(color, ZERO)
    x5 = compose(flip, x4)
    x6 = sfilter(x3, x5)
    x7 = sizefilter(x6, ONE)
    x8 = merge(x7)
    x9 = fill(grid, ONE, x8)
    return x9


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
