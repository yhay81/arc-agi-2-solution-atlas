def components(g, background=None, by_color=True, diagonal=False):
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if diagonal:
        offsets += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    h, w = (len(g), len(g[0]))
    unseen = {(r, c) for r in range(h) for c in range(w) if g[r][c] != background}
    result = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        queue = [start]
        cells = []
        color = g[start[0]][start[1]]
        while queue:
            r, c = queue.pop()
            cells.append((r, c))
            for dr, dc in offsets:
                p = (r + dr, c + dc)
                if p in unseen and (not by_color or g[p[0]][p[1]] == color):
                    unseen.remove(p)
                    queue.append(p)
        result.append((color, cells))
    return result


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    out = [[8] * w for _ in range(h)]
    for _, cells in components(g, 8, False, True):
        colored = [(r, c) for r, c in cells if g[r][c] != 1]
        centers = [
            (r, c)
            for r, c in colored
            if all(((r + dr, c + dc) in colored for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]))
        ]
        if len(centers) != 1 or len(colored) != 5:
            raise ValueError("Expected one colored cross per trail")
        r, c = centers[0]
        blues = [p for p in cells if g[p[0]][p[1]] == 1]
        if all((b < c for a, b in blues)):
            dr, dc = (0, 1)
            steps = w - 2 - c
        elif all((b > c for a, b in blues)):
            dr, dc = (0, -1)
            steps = c - 1
        elif all((a < r for a, b in blues)):
            dr, dc = (1, 0)
            steps = h - 2 - r
        elif all((a > r for a, b in blues)):
            dr, dc = (-1, 0)
            steps = r - 1
        else:
            raise ValueError("Trail direction not unique")
        for a, b in cells:
            color = g[a][b]
            if color != 1:
                a, b = (2 * r - a, 2 * c - b)
            out[a + steps * dr][b + steps * dc] = color
    return out
