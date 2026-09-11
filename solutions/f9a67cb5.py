def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = copy(g)
    out = copy(g)
    h, w = (len(g), len(g[0]))
    start = next(((r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == 2))
    if start[1] not in (0, w - 1):
        result = solve([list(row) for row in zip(*g)])
        return [list(row) for row in zip(*result)]
    direction = 1 if start[1] == 0 else -1
    todo = [start]
    visited = set()
    while todo:
        r, c = todo.pop()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        while 0 <= c < w and g[r][c] != 8:
            out[r][c] = 2
            c += direction
        if not 0 <= c < w:
            continue
        wall = c
        before = c - direction
        for dr in (-1, 1):
            a = r
            while 0 <= a < h:
                out[a][before] = 2
                if g[a][wall] != 8:
                    todo.append((a, wall))
                    break
                a += dr
    return out
