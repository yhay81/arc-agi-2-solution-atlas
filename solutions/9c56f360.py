def solve(grid):
    g = grid
    out = [r[:] for r in g]
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            if v != 3:
                continue
            target = c
            while target > 0 and out[r][target - 1] == 0:
                target -= 1
            out[r][c] = 0
            out[r][target] = 3
    return out
