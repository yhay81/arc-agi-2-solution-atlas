"""Executable re-arc DSL program for ARC-AGI-2 task d406998b.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    THREE,
    compose,
    double,
    equality,
    fgpartition,
    fill,
    fork,
    halve,
    identity,
    last,
    merge,
    sfilter,
    toindices,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "d406998b"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = vmirror(grid)
    x1 = fgpartition(x0)
    x2 = merge(x1)
    x3 = toindices(x2)
    x4 = compose(double, halve)
    x5 = fork(equality, identity, x4)
    x6 = compose(x5, last)
    x7 = sfilter(x3, x6)
    x8 = fill(x0, THREE, x7)
    x9 = vmirror(x8)
    return x9


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
