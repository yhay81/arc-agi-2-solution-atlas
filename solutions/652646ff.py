from collections import Counter


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    background = bg(g)
    h, w = (len(g), len(g[0]))
    shape = (
        (0, 2),
        (0, 3),
        (1, 1),
        (1, 4),
        (2, 0),
        (2, 5),
        (3, 0),
        (3, 5),
        (4, 1),
        (4, 4),
        (5, 2),
        (5, 3),
    )
    counts = Counter(v for row in g for v in row if v != background)
    rings = {}
    for color, n in counts.items():
        if n < 5:
            continue
        options = []
        for a in range(-5, h):
            for c in range(-5, w):
                cells = {(a + dr, c + dc) for dr, dc in shape}
                matches = sum(
                    (0 <= r < h and 0 <= col < w and (g[r][col] == color) for r, col in cells)
                )
                if matches >= 5:
                    options.append((matches, a, c, cells))
        if options:
            rings[color] = max(options, key=lambda x: x[0])[3]
    edges = set()
    for x in rings:
        for y in rings:
            if x == y:
                continue
            if any((0 <= r < h and 0 <= c < w and (g[r][c] == x) for r, c in rings[x] & rings[y])):
                edges.add((x, y))
    order = []
    remaining = set(rings)
    while remaining:
        ready = [x for x in remaining if not any((b == x and a in remaining for a, b in edges))]
        if len(ready) != 1:
            raise ValueError(("Layer order ambiguous", ready))
        order += ready
        remaining.remove(ready[0])
    out = []
    for color in order:
        tile = [[background] * 6 for _ in range(6)]
        for r, c in shape:
            tile[r][c] = color
        out += tile
    return out
