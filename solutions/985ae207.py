from collections import Counter


def cp(g):
    return [row[:] for row in g]


def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def components(g, background=0, diagonal=False, mono=True):
    unseen = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != background}
    out = []
    while unseen:
        p = min(unseen)
        unseen.remove(p)
        q = [p]
        cells = []
        for r, c in q:
            cells.append((r, c))
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if not (dr or dc) or (not diagonal and dr and dc):
                        continue
                    n = (r + dr, c + dc)
                    if n in unseen and (not mono or g[n[0]][n[1]] == g[r][c]):
                        unseen.remove(n)
                        q.append(n)
        out.append(cells)
    return out


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    background = bg(g)
    objects = components(g, background, False, False)
    stamps = []
    walls = []
    for obj in objects:
        a, b, c, d = bbox(obj)
        colors = {g[r][col] for r, col in obj}
        if (
            b - a == 2
            and d - c == 2
            and (len(colors) == 2)
            and all(
                g[r][col] == g[a][c]
                for r in range(a, b + 1)
                for col in range(c, d + 1)
                if (r, col) != (a + 1, c + 1)
            )
        ):
            stamps.append((a + 1, c + 1, g[a][c], g[a + 1][c + 1]))
        elif len(colors) == 1:
            walls.append((a, b, c, d, next(iter(colors))))
    out = cp(g)
    for r, c, border, center in stamps:
        matches = [
            wall
            for wall in walls
            if wall[4] == center and (wall[0] <= r <= wall[1] or wall[2] <= c <= wall[3])
        ]
        if len(matches) != 1:
            raise ValueError("Matching bar not unique")
        a, b, left, right, _ = matches[0]
        dr, dc = (0, 1 if c < left else -1) if a <= r <= b else (1 if r < a else -1, 0)
        while True:
            for rr in range(r - 1, r + 2):
                for cc in range(c - 1, c + 2):
                    put(out, rr, cc, center if (rr, cc) == (r, c) else border)
            if a <= r <= b and left <= c <= right:
                break
            r += dr * 3
            c += dc * 3
            if not (0 <= r < len(g) and 0 <= c < len(g[0])):
                raise ValueError("Stamp never reaches bar")
    return out
