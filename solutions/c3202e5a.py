from itertools import pairwise


def solve(grid):
    height, width = len(grid), len(grid[0])
    rows = [r for r, row in enumerate(grid) if len(set(row)) == 1 and row[0] != 0]
    cols = [c for c in range(width) if len({row[c] for row in grid}) == 1 and grid[0][c] != 0]
    if not rows or not cols:
        raise ValueError("Missing full grid separator rows or columns")
    boundaries_r, boundaries_c = [-1, *rows, height], [-1, *cols, width]
    candidates = []
    for a, b in pairwise(boundaries_r):
        for c, d in pairwise(boundaries_c):
            if b <= a + 1 or d <= c + 1:
                continue
            patch = [row[c + 1 : d] for row in grid[a + 1 : b]]
            if len({v for row in patch for v in row} - {0}) == 1:
                candidates.append(patch)
    if len(candidates) != 1:
        raise ValueError("Expected one monochromatic nonempty panel")
    return candidates[0]
