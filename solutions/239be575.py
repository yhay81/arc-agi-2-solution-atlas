"""Executable re-arc DSL program for ARC-AGI-2 task 239be575.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    EIGHT,
    ONE,
    TWO,
    UNITY,
    ZERO,
    F,
    T,
    adjacent,
    apply,
    both,
    branch,
    canvas,
    chain,
    colorcount,
    colorfilter,
    compose,
    extract,
    first,
    fork,
    last,
    lbind,
    matcher,
    normalize,
    objects,
    palette,
    positive,
    rbind,
    remove,
    sfilter,
    size,
    totuple,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "239be575"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, F)
    x1 = lbind(apply, normalize)
    x2 = lbind(colorfilter, x0)
    x3 = chain(size, x1, x2)
    x4 = matcher(x3, ONE)
    x5 = lbind(colorcount, grid)
    x6 = matcher(x5, EIGHT)
    x7 = lbind(colorfilter, x0)
    x8 = compose(size, x7)
    x9 = matcher(x8, TWO)
    x10 = fork(both, x6, x9)
    x11 = fork(both, x10, x4)
    x12 = palette(grid)
    x13 = extract(x12, x11)
    x14 = colorfilter(x0, x13)
    x15 = totuple(x14)
    x16 = first(x15)
    x17 = last(x15)
    x18 = palette(grid)
    x19 = remove(ZERO, x18)
    x20 = remove(x13, x19)
    x21 = first(x20)
    x22 = colorfilter(x0, x21)
    x23 = rbind(adjacent, x16)
    x24 = rbind(adjacent, x17)
    x25 = fork(both, x23, x24)
    x26 = sfilter(x22, x25)
    x27 = size(x26)
    x28 = positive(x27)
    x29 = branch(x28, x21, ZERO)
    x30 = canvas(x29, UNITY)
    return x30


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
