"""Executable re-arc DSL program for ARC-AGI-2 task b230c067.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    ONE,
    TWO,
    T,
    argmin,
    chain,
    compose,
    fill,
    lbind,
    matcher,
    merge,
    normalize,
    objects,
    remove,
    sfilter,
    size,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "b230c067"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, T, T)
    x1 = lbind(sfilter, x0)
    x2 = lbind(matcher, normalize)
    x3 = compose(x2, normalize)
    x4 = chain(size, x1, x3)
    x5 = argmin(x0, x4)
    x6 = remove(x5, x0)
    x7 = merge(x6)
    x8 = fill(grid, TWO, x5)
    x9 = fill(x8, ONE, x7)
    return x9


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
