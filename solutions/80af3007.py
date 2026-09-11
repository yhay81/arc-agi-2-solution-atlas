from collections import Counter
from math import isqrt


def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = Counter(v for row in grid for v in row).most_common(1)[0][0]
    pts = [(r, c) for r in range(h) for c in range(w) if grid[r][c] != bg]
    if not pts:
        return [r[:] for r in grid]
    t, l = min(r for r, _ in pts), min(c for _, c in pts)
    b, r = max(x for x, _ in pts), max(y for _, y in pts)
    crop = [row[l : r + 1] for row in grid[t : b + 1]]
    vals = {v for row in grid for v in row if v}
    if len(vals) != 1 or len(crop) != len(crop[0]):
        return [r[:] for r in grid]
    n = isqrt(len(crop))
    color = next(iter(vals))
    if n < 2 or n * n != len(crop):
        return [r[:] for r in grid]
    compact = []
    for i in range(n):
        line = []
        for j in range(n):
            block = [crop[x][j * n : (j + 1) * n] for x in range(i * n, (i + 1) * n)]
            if all(v == color for row in block for v in row):
                line.append(1)
            elif any(v != 0 for row in block for v in row):
                return [r[:] for r in grid]
            else:
                line.append(0)
        compact.append(line)
    return [
        [compact[i][j] * compact[k][q] * color for j in range(n) for q in range(n)]
        for i in range(n)
        for k in range(n)
    ]
