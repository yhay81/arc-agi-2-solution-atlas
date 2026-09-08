"""Executable program for ARC-AGI-2 task c074846d.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

TASK_ID = "c074846d"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("verified-program",)


def solve_c074846d(grid):
    pivots = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 5]
    if len(pivots) != 1:
        raise ValueError("Expected exactly one gray pivot")
    pr, pc = pivots[0]
    red = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 2]
    out = [row[:] for row in grid]
    for r, c in red:
        out[r][c] = 3
    for r, c in red:
        nr, nc = pr + c - pc, pc - r + pr
        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
            raise ValueError("Rotated red line would leave the grid")
        out[nr][nc] = 2
    return out


solve = solve_c074846d
