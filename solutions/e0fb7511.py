"""Executable program for ARC-AGI-2 task e0fb7511.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

TASK_ID = "e0fb7511"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("verified-program",)


def solve_e0fb7511(grid):
    remaining = {(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 0}
    out = [row[:] for row in grid]
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        component, stack = {start}, [start]
        while stack:
            r, c = stack.pop()
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in remaining:
                    remaining.remove(point)
                    component.add(point)
                    stack.append(point)
        if len(component) >= 2:
            for r, c in component:
                out[r][c] = 8
    return out


solve = solve_e0fb7511
