"""Executable re-arc DSL program for ARC-AGI-2 task 4c5c2cf0.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FIVE,
    backdrop,
    both,
    center,
    chain,
    color,
    compose,
    difference,
    dneighbors,
    equality,
    extract,
    fgpartition,
    first,
    fork,
    hmirror,
    identity,
    initset,
    insert,
    lbind,
    mapply,
    matcher,
    merge,
    paint,
    rapply,
    rbind,
    sfilter,
    shift,
    size,
    subtract,
    toindices,
    ulcorner,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "4c5c2cf0"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = compose(dneighbors, center)
    x2 = fork(difference, backdrop, x1)
    x3 = fork(equality, toindices, x2)
    x4 = matcher(size, FIVE)
    x5 = fork(both, x3, x4)
    x6 = extract(x0, x5)
    x7 = color(x6)
    x8 = merge(x0)
    x9 = compose(hmirror, vmirror)
    x10 = initset(x9)
    x11 = insert(vmirror, x10)
    x12 = insert(hmirror, x11)
    x13 = rapply(x12, x8)
    x14 = ulcorner(x6)
    x15 = lbind(subtract, x14)
    x16 = matcher(first, x7)
    x17 = rbind(sfilter, x16)
    x18 = chain(x15, ulcorner, x17)
    x19 = fork(shift, identity, x18)
    x20 = mapply(x19, x13)
    x21 = paint(grid, x20)
    return x21


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
