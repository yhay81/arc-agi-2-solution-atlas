"""Executable program for ARC-AGI-2 task ccd554ac.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

TASK_ID = "ccd554ac"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("verified-program",)


def solve_ccd554ac(grid):
    height, width = len(grid), len(grid[0])
    return [
        [grid[r % height][c % width] for c in range(width * width)] for r in range(height * height)
    ]


solve = solve_ccd554ac
