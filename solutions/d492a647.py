"""Executable program for ARC-AGI-2 task d492a647.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

TASK_ID = "d492a647"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("verified-program",)


def solve_d492a647(grid):
    points = [(r, c, v) for r, row in enumerate(grid) for c, v in enumerate(row) if v not in (0, 5)]
    if len(points) != 1:
        raise ValueError("Expected one colored seed point")
    pr, pc, color = points[0]
    out = [row[:] for row in grid]
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == 0 and (r - pr) % 2 == 0 and (c - pc) % 2 == 0:
                out[r][c] = color
    return out


solve = solve_d492a647
