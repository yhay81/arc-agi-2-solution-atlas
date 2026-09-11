def solve(grid):
    g = grid
    sep = next((r for r, row in enumerate(g) if len(set(row)) == 1 and row[0] == 5))
    tile = g[:sep]
    mask = g[sep + 1 :]
    rows = [r for r in range(len(tile)) if r == 0 or tile[r] != tile[r - 1]]
    cols = [c for c in range(len(tile[0])) if c == 0 or any(row[c] != row[c - 1] for row in tile)]
    tile = [[tile[r][c] for c in cols] for r in rows]
    ph, pw = (len(tile), len(tile[0]))
    o = [[0] * (len(mask[0]) * pw) for _ in range(len(mask) * ph)]
    for r, row in enumerate(mask):
        for c, v in enumerate(row):
            if v == 2:
                for i in range(ph):
                    for j in range(pw):
                        o[r * ph + i][c * pw + j] = tile[i][j]
    return o
