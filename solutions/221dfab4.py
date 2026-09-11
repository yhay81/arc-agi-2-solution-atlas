from collections import Counter


def solve(grid):
    grid = [row[:] for row in grid]
    h, w = (len(grid), len(grid[0]))
    points = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 4]
    bg = Counter(v for row in grid for v in row).most_common(1)[0][0]
    rs = {r for r, c in points}
    cs = {c for r, c in points}
    out = [row[:] for row in grid]
    if len(rs) == 1 and next(iter(rs)) in (0, h - 1):
        ar = next(iter(rs))
        step = 1 if ar == 0 else -1
        for r in range(h):
            d = (r - ar) * step
            val = [4, bg, 4, bg, 3, bg][d % 6]
            for c in range(w):
                if c in cs:
                    out[r][c] = val
                elif val == 3 and grid[r][c] != bg:
                    out[r][c] = 3
    elif len(cs) == 1 and next(iter(cs)) in (0, w - 1):
        result = solve([list(row) for row in zip(*grid)])
        return [list(row) for row in zip(*result)]
    else:
        raise ValueError("Expected single boundary stripe of color 4")
    return out
