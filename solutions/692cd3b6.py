def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    centers = [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 5]
    ends = []
    for r, c in centers:
        options = [
            (r + dr, c + dc)
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))
            if g[r + dr][c + dc] == 0
        ]
        if len(options) != 1:
            raise ValueError("exit around the gray area is not unique")
        ends.append(options[0])
    if len(ends) != 2:
        raise ValueError("there are not exactly two exits")

    def distances(start):
        q = [start]
        ds = {start: 0}
        for r, c in q:
            for a, b in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= a < h and 0 <= b < w and (g[a][b] == 0) and ((a, b) not in ds):
                    ds[a, b] = ds[r, c] + 1
                    q.append((a, b))
        return ds

    a, b = map(distances, ends)
    n = a[ends[1]]
    out = copy(g)
    for p, d in a.items():
        if p in b and d + b[p] == n:
            out[p[0]][p[1]] = 4
    return out
