"""Executable re-arc DSL program for ARC-AGI-2 task e26a3af2.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    apply,
    branch,
    compose,
    dedupe,
    greater,
    height,
    hupscale,
    mostcommon,
    repeat,
    rot90,
    size,
    vupscale,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "e26a3af2"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = rot90(grid)
    x1 = apply(mostcommon, grid)
    x2 = apply(mostcommon, x0)
    x3 = repeat(x1, ONE)
    x4 = repeat(x2, ONE)
    x5 = compose(size, dedupe)
    x6 = x5(x1)
    x7 = x5(x2)
    x8 = greater(x7, x6)
    x9 = branch(x8, height, width)
    x10 = x9(grid)
    x11 = rot90(x3)
    x12 = branch(x8, x4, x11)
    x13 = branch(x8, vupscale, hupscale)
    x14 = x13(x12, x10)
    return x14


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
