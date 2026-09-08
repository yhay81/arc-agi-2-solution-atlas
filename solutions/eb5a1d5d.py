"""Executable re-arc DSL program for ARC-AGI-2 task eb5a1d5d.

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
    compose,
    dedupe,
    dmirror,
    fork,
    hmirror,
    identity,
    last,
    remove,
    vconcat,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "eb5a1d5d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = compose(dmirror, dedupe)
    x1 = x0(grid)
    x2 = x0(x1)
    x3 = fork(remove, last, identity)
    x4 = compose(hmirror, x3)
    x5 = fork(vconcat, identity, x4)
    x6 = x5(x2)
    x7 = dmirror(x6)
    x8 = x5(x7)
    return x8


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
