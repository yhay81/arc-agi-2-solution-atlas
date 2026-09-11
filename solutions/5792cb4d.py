def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    cells = set(((r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != 8))

    def neighbors(p):
        r, c = p
        return cells & {(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)}

    ends = [p for p in cells if len(neighbors(p)) == 1]
    if len(ends) != 2 or any(len(neighbors(p)) > 2 for p in cells):
        raise ValueError("Expected single nonbranching path")
    path = [min(ends)]
    used = set(path)
    while len(path) < len(cells):
        candidates = neighbors(path[-1]) - used
        if len(candidates) != 1:
            raise ValueError("Disconnected path")
        p = candidates.pop()
        path.append(p)
        used.add(p)
    out = cp(g)
    for (r, c), (a, b) in zip(path, path[::-1]):
        out[r][c] = g[a][b]
    return out
