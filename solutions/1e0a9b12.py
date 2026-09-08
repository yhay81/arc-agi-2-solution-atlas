"""Executable re-arc DSL program for ARC-AGI-2 task 1e0a9b12.

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
    apply,
    combine,
    compose,
    flip,
    fork,
    identity,
    matcher,
    mostcolor,
    rbind,
    rot90,
    rot270,
    sfilter,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "1e0a9b12"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = mostcolor(grid)
    x1 = rot270(grid)
    x2 = matcher(identity, x0)
    x3 = rbind(sfilter, x2)
    x4 = compose(flip, x2)
    x5 = rbind(sfilter, x4)
    x6 = fork(combine, x3, x5)
    x7 = apply(x6, x1)
    x8 = rot90(x7)
    return x8


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
