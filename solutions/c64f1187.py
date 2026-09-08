"""Executable program for ARC-AGI-2 task c64f1187.

Evidence:
- The program matches every provided training and test pair exactly.
- Provided test outputs were available during acceptance.

This entry was promoted from the private workbench and still requires an
independent editorial review of its general rule.
"""

TASK_ID = "c64f1187"
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


def solve_c64f1187(grid):
    gray = {(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 5}
    if not gray:
        raise ValueError("Missing gray target cells")
    top, bottom, left, right = bounds(gray)
    dictionary = {}
    for r in range(top):
        for c, color in enumerate(grid[r]):
            if color not in (0, 1, 5):
                patch = [[grid[r + dr][c + dc] == 1 for dc in (1, 2)] for dr in (1, 2)]
                if color in dictionary or not any(any(row) for row in patch):
                    raise ValueError("Ambiguous template color or empty blue template")
                dictionary[color] = patch
    out = [[0] * (right - left + 1) for _ in range(bottom - top + 1)]
    for group in components(gray):
        a, b, c, d = bounds(group)
        if b - a != 1 or d - c != 1:
            raise ValueError("Expected two by two gray target blocks")
        colors = {grid[r][col] for r in range(a, b + 1) for col in range(c, d + 1)} - {0, 5}
        if not colors:
            continue
        if len(colors) != 1:
            raise ValueError("Ambiguous target block color")
        color = next(iter(colors))
        patch = dictionary[color]
        for dr in range(2):
            for dc in range(2):
                out[a - top + dr][c - left + dc] = color if patch[dr][dc] else 0
    return out


solve = solve_c64f1187
