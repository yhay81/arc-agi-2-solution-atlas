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


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def solve(grid):
    g = grid
    background = bg(g)
    objs = components(g, background, False, True)
    centers = [(sum((r for r, c in o)) / len(o), sum((c for r, c in o)) / len(o)) for o in objs]
    vertical = max((r for r, c in centers)) - min((r for r, c in centers)) > max(
        (c for r, c in centers)
    ) - min((c for r, c in centers))
    objs.sort(key=lambda o: sum((r if vertical else c for r, c in o)) / len(o))
    bullet = objs[1]
    ends = [objs[0], objs[2]]
    bulletcolor = g[bullet[0][0]][bullet[0][1]]

    def rectangular(o):
        a, b, c, d = bbox(o)
        return len(o) == (b - a + 1) * (d - c + 1)

    irregular = [o for o in ends if not rectangular(o)]
    if len(irregular) == 1:
        gun = irregular[0]
        target = next(o for o in ends if o is not gun)
    else:
        target = max(
            ends, key=lambda o: bbox(o)[3] - bbox(o)[2] if vertical else bbox(o)[1] - bbox(o)[0]
        )
        gun = next(o for o in ends if o is not target)
    a, b, c, d = bbox(bullet)
    gr = sum((r for r, c in gun)) / len(gun)
    gc = sum((c for r, c in gun)) / len(gun)
    br, bc = ((a + b) / 2, (c + d) / 2)
    sign = 1 if (br - gr if vertical else bc - gc) > 0 else -1
    out = cp(g)
    for r, col in bullet + target:
        out[r][col] = background
    for r, col in target:
        axis = col if vertical else r
        center = bc if vertical else br
        shift = (d - c + 1) // 2 if vertical else (b - a + 1) // 2
        delta = shift if axis > center else -shift
        put(out, r if vertical else r + delta, col + delta if vertical else col, g[r][col])
    tr = (len(g) - (b - a + 1) if sign > 0 else 0) if vertical else a
    tc = c if vertical else len(g[0]) - (d - c + 1) if sign > 0 else 0
    for dr in range(b - a + 1):
        for dc in range(d - c + 1):
            out[tr + dr][tc + dc] = bulletcolor
    return out
