"""Executable re-arc DSL program for ARC-AGI-2 task 90c28cc7.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    ZERO,
    chain,
    compose,
    dedupe,
    dmirror,
    flip,
    identity,
    matcher,
    positive,
    power,
    rbind,
    sfilter,
    size,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "90c28cc7"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = matcher(identity, ZERO)
    x1 = compose(flip, x0)
    x2 = rbind(sfilter, x1)
    x3 = chain(positive, size, x2)
    x4 = rbind(sfilter, x3)
    x5 = compose(dmirror, x4)
    x6 = power(x5, FOUR)
    x7 = x6(grid)
    x8 = dedupe(x7)
    x9 = dmirror(x8)
    x10 = dedupe(x9)
    x11 = dmirror(x10)
    return x11


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
