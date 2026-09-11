from collections import Counter


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
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    background = bg(g)
    objs = components(g, background, False, True)
    rects = [bbox(o) for o in objs]
    filled = set()
    edges = []
    for a, b, c, d in rects:
        filled |= {(r, col) for r in range(a, b + 1) for col in range(c, d + 1)}
    for i, (a, b, c, d) in enumerate(rects):
        for j, (e, f, k, l) in enumerate(rects):
            if j <= i:
                continue
            if max(a, e) + 1 <= min(b, f) - 1 and (d < k or l < c):
                left, right = sorted([(a, b, c, d), (e, f, k, l)], key=lambda q: q[2])
                gap = right[2] - left[3]
                cells = {
                    (r, col)
                    for r in range(max(a, e) + 1, min(b, f))
                    for col in range(left[3], right[2] + 1)
                }
                edges.append((gap, i, j, cells))
            if max(c, k) + 1 <= min(d, l) - 1 and (b < e or f < a):
                top, bottom = sorted([(a, b, c, d), (e, f, k, l)])
                gap = bottom[0] - top[1]
                cells = {
                    (r, col)
                    for r in range(top[1], bottom[0] + 1)
                    for col in range(max(c, k) + 1, min(d, l))
                }
                edges.append((gap, i, j, cells))
    parent = list(range(len(rects)))

    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i

    for gap, i, j, cells in sorted(edges, key=lambda x: x[0]):
        if find(i) == find(j):
            continue
        parent[find(i)] = find(j)
        filled |= cells
    color = g[objs[0][0][0]][objs[0][0][1]]
    out = [[background] * w for _ in range(h)]
    for r, c in filled:
        if any(
            (r + dr, c + dc) not in filled for dr in (-1, 0, 1) for dc in (-1, 0, 1) if dr or dc
        ):
            out[r][c] = color
    return out
