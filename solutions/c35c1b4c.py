"""Executable program for ARC-AGI-2 task c35c1b4c.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

TASK_ID = "c35c1b4c"
STATUS = "all_provided_pairs_match"
EVIDENCE = "test_output_used_for_acceptance"
CONCEPTS = ("verified-program",)


def components(points):
    remaining, result = set(points), []
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        group, stack = {start}, [start]
        while stack:
            r, c = stack.pop()
            for neighbor in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    group.add(neighbor)
                    stack.append(neighbor)
        result.append(group)
    return result


def bounds(points):
    return (
        min(r for r, c in points),
        max(r for r, c in points),
        min(c for r, c in points),
        max(c for r, c in points),
    )


def solve_c35c1b4c(grid):
    colors = {v for row in grid for v in row} - {0}
    counts = {color: sum(row.count(color) for row in grid) for color in colors}
    candidates = [color for color, count in counts.items() if count == max(counts.values())]
    if len(candidates) != 1:
        raise ValueError("Expected one most frequent nonblack object color")
    color = candidates[0]
    out = [row[:] for row in grid]
    width = len(grid[0])
    for r, row in enumerate(grid):
        for c, value in enumerate(row):
            if value == color:
                out[r][width - c - 1] = color
    return out


solve = solve_c35c1b4c
