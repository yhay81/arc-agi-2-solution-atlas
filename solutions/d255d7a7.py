from collections import Counter


def cp(g):
    return [row[:] for row in g]


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
    h, w = (len(g), len(g[0]))
    out = cp(g)
    background = bg(g)
    blacks = components([[0 if v == 0 else -1 for v in row] for row in g], -1, False, True)
    moves = []
    for obj in blacks:
        a, b, c, d = bbox(obj)
        horizontal = d - c > b - a
        counts = Counter((col if horizontal else r for r, col in obj))
        fat = [x for x, n in counts.items() if n > 1]
        lo, hi = (min(fat), max(fat))
        top, bottom, left, right = (a, b, lo, hi) if horizontal else (lo, hi, c, d)
        dest_r = top if horizontal else h - (bottom - top + 1) if top == 0 else 0
        dest_c = (w - (right - left + 1) if left == 0 else 0) if horizontal else left
        block = [row[left : right + 1] for row in g[top : bottom + 1]]
        moves.append((dest_r, dest_c, block))
        for r, col in obj:
            out[r][col] = background
        for r in range(top, bottom + 1):
            for col in range(left, right + 1):
                out[r][col] = background
    for top, left, block in moves:
        for r, row in enumerate(block):
            for c, v in enumerate(row):
                out[top + r][left + c] = v
    return out
