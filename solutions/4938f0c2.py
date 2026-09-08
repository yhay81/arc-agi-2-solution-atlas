"""Executable re-arc DSL program for ARC-AGI-2 task 4938f0c2.

Evidence:
- This program matches every provided training and test pair exactly.
- Provided test outputs were used only for acceptance verification.

Source:
- re-arc verifiers.py, distributed under the MIT License.
"""

from arc_agi_2_atlas.re_arc_dsl import (
    FOUR,
    both,
    chain,
    color,
    compose,
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
    square,
    subtract,
    ulcorner,
    vmirror,
)
from arc_agi_2_atlas.re_arc_dsl import (
    Grid as ReArcGrid,
)
from arc_agi_2_atlas.types import Grid

TASK_ID = "4938f0c2"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("re-arc", "dsl-program")


def _program(grid: ReArcGrid) -> ReArcGrid:
    x0 = fgpartition(grid)
    x1 = matcher(size, FOUR)
    x2 = fork(both, square, x1)
    x3 = extract(x0, x2)
    x4 = color(x3)
    x5 = merge(x0)
    x6 = compose(hmirror, vmirror)
    x7 = initset(x6)
    x8 = insert(vmirror, x7)
    x9 = insert(hmirror, x8)
    x10 = rapply(x9, x5)
    x11 = ulcorner(x3)
    x12 = lbind(subtract, x11)
    x13 = matcher(first, x4)
    x14 = rbind(sfilter, x13)
    x15 = chain(x12, ulcorner, x14)
    x16 = fork(shift, identity, x15)
    x17 = mapply(x16, x10)
    x18 = paint(grid, x17)
    return x18


def solve(grid: Grid) -> Grid:
    """Run the DSL program and return a mutable grid."""
    immutable = tuple(tuple(row) for row in grid)
    return [list(row) for row in _program(immutable)]
