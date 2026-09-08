"""Executable program for ARC-AGI-2 task d19f7514.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

TASK_ID = "d19f7514"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("verified-program",)


def solve_d19f7514(grid):
    if len(grid) % 2:
        raise ValueError("Expected equally sized upper and lower panels")
    half = len(grid) // 2
    return [
        [0 if grid[r][c] == grid[r + half][c] == 0 else 4 for c in range(len(grid[0]))]
        for r in range(half)
    ]


solve = solve_d19f7514
