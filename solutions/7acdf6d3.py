def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


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
    choices = []
    for vessel_color, grain_color in [(2, 9), (9, 2)]:
        vessels = components(
            [[vessel_color if v == vessel_color else 7 for v in row] for row in g], 7, True, True
        )
        n = len(points(g, grain_color))
        for o in vessels:
            a, b, c, d = bbox(o)
            inside = []
            valid = True
            for r in range(a, b):
                cs = sorted((col for rr, col in o if rr == r))
                if len(cs) != 2:
                    valid = False
                    break
                inside.extend((r, col) for col in range(cs[0] + 1, cs[1]))
            if valid and len(inside) == n and inside:
                choices.append((grain_color, inside))
    if len(choices) != 1:
        raise ValueError("Expected unique matching vessel")
    color, inside = choices[0]
    out = [[7 if v == color else v for v in row] for row in g]
    for r, c in inside:
        out[r][c] = color
    return out
