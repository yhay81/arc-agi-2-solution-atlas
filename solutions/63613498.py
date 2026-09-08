"""Executable re-arc DSL program for ARC-AGI-2 task 63613498.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    TWO,
    F,
    T,
    add,
    argmax,
    bordering,
    both,
    chain,
    color,
    compose,
    decrement,
    delta,
    equality,
    fill,
    first,
    flip,
    fork,
    height,
    matcher,
    mostcolor,
    normalize,
    numcolors,
    objects,
    rbind,
    remove,
    sfilter,
    size,
    toindices,
    toobject,
    width,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "63613498"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = objects(grid, T, F, T)
    x1 = mostcolor(grid)
    x2 = fork(add, height, width)
    x3 = compose(decrement, x2)
    x4 = fork(equality, x3, size)
    x5 = rbind(bordering, grid)
    x6 = fork(both, x4, x5)
    x7 = rbind(toobject, grid)
    x8 = chain(numcolors, x7, delta)
    x9 = matcher(x8, TWO)
    x10 = fork(both, x6, x9)
    x11 = sfilter(x0, x10)
    x12 = argmax(x11, size)
    x13 = delta(x12)
    x14 = toobject(x13, grid)
    x15 = matcher(first, x1)
    x16 = compose(flip, x15)
    x17 = sfilter(x14, x16)
    x18 = normalize(x17)
    x19 = toindices(x18)
    x20 = compose(toindices, normalize)
    x21 = matcher(x20, x19)
    x22 = remove(x17, x0)
    x23 = argmax(x22, x21)
    x24 = color(x12)
    x25 = fill(grid, x24, x23)
    return x25


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
