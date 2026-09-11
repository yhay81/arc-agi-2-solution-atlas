def solve(grid):
    a = grid
    n = sum(v == 5 for row in a for v in row)
    cols = [
        c for c in range(len(a[0])) if len({row[c] for row in a}) == 1 and a[0][c] not in (0, 5)
    ]
    if not (cols and n > 0):
        raise ValueError("task assumptions are not satisfied")
    colors = [a[0][c] for c in cols]
    out = [row[:] for row in a]
    for row in out:
        for c in cols:
            row[c] = 0
    for r in range(len(a)):
        out[r][min(cols) - 1] = colors[r // n % len(colors)]
    return out
