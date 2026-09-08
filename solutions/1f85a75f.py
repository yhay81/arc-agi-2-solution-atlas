"""Executable re-arc DSL program for ARC-AGI-2 task 1f85a75f.

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
    apply,
    argmax,
    chain,
    color,
    colorcount,
    extract,
    identity,
    lbind,
    matcher,
    objects,
    sfilter,
    size,
    subgrid,
    totuple,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "1f85a75f"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = totuple(x0)
    x2 = apply(color, x1)
    x3 = lbind(sfilter, x2)
    x4 = lbind(matcher, identity)
    x5 = chain(size, x3, x4)
    x6 = matcher(x5, ONE)
    x7 = sfilter(x2, x6)
    x8 = lbind(colorcount, grid)
    x9 = argmax(x7, x8)
    x10 = matcher(color, x9)
    x11 = extract(x0, x10)
    x12 = subgrid(x11, grid)
    return x12


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
