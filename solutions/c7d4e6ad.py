"""Executable program for ARC-AGI-2 task c7d4e6ad.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

TASK_ID = "c7d4e6ad"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("verified-program",)


def solve_c7d4e6ad(grid):
    out = [row[:] for row in grid]
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == 5:
                if grid[r][0] in (0, 5):
                    raise ValueError("Gray cell has no row color instruction")
                out[r][c] = grid[r][0]
    return out


solve = solve_c7d4e6ad
