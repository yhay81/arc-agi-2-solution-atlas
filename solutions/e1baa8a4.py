"""Executable program for ARC-AGI-2 task e1baa8a4.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

TASK_ID = "e1baa8a4"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("verified-program",)


def solve_e1baa8a4(grid):
    rows = [0] + [r for r in range(1, len(grid)) if grid[r] != grid[r - 1]]
    cols = [0] + [c for c in range(1, len(grid[0])) if any(row[c] != row[c - 1] for row in grid)]
    return [[grid[r][c] for c in cols] for r in rows]


solve = solve_e1baa8a4
