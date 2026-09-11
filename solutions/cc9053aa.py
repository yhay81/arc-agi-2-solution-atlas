def cp(g):
    return [row[:] for row in g]


def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


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


def solve(grid):
    g = grid
    start, end = points(g, 9)
    h, w = (len(g), len(g[0]))
    allowed = set()
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            if v not in (8, 9):
                continue
            if any(
                0 <= r + dr < h and 0 <= c + dc < w and (g[r + dr][c + dc] == 7)
                for dr in (-1, 0, 1)
                for dc in (-1, 0, 1)
                if dr or dc
            ):
                continue
            allowed.add((r, c))
    out = cp(g)
    for r, c in shortest_path_cells(g, start, end, allowed):
        out[r][c] = 9
    return out
