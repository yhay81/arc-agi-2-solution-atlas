"""Executable re-arc DSL program for ARC-AGI-2 task 3bdb4ada.

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
    both,
    chain,
    color,
    compose,
    equality,
    even,
    extract,
    fill,
    first,
    flip,
    fork,
    height,
    last,
    lbind,
    leftmost,
    mapply,
    multiply,
    partition,
    rbind,
    remove,
    sfilter,
    size,
    subtract,
    toindices,
    uppermost,
    width,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "3bdb4ada"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = partition(grid)
    x1 = fork(multiply, height, width)
    x2 = fork(equality, size, x1)
    x3 = compose(flip, x2)
    x4 = extract(x0, x3)
    x5 = remove(x4, x0)
    x6 = compose(flip, even)
    x7 = rbind(chain, first)
    x8 = rbind(chain, last)
    x9 = lbind(rbind, subtract)
    x10 = lbind(x7, x6)
    x11 = lbind(x8, x6)
    x12 = chain(x10, x9, uppermost)
    x13 = chain(x11, x9, leftmost)
    x14 = lbind(fork, both)
    x15 = fork(x14, x12, x13)
    x16 = fork(sfilter, toindices, x15)
    x17 = mapply(x16, x5)
    x18 = color(x4)
    x19 = fill(grid, x18, x17)
    return x19


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
