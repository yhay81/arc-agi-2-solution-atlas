def shortest_path_cells(g, start, end, allowed):
    h, w = (len(g), len(g[0]))

    def distances(origin):
        dist = {origin: 0}
        queue = [origin]
        for r, c in queue:
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                p = (r + dr, c + dc)
                if p in allowed and p not in dist:
                    dist[p] = dist[r, c] + 1
                    queue.append(p)
        return dist

    ds, de = (distances(start), distances(end))
    if end not in ds:
        raise ValueError("Endpoints disconnected")
    return {p for p in ds if p in de and ds[p] + de[p] == ds[end]}


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    start, end = points(g, 2)
    allowed = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v in (0, 2)}
    out = cp(g)
    for r, c in shortest_path_cells(g, start, end, allowed):
        if g[r][c] == 0:
            out[r][c] = 4
    return out
