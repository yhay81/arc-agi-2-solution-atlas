from collections import Counter


def comps(mask):
    h, w = len(mask), len(mask[0])
    unseen = {(r, c) for r in range(h) for c in range(w) if mask[r][c]}
    out = []
    while unseen:
        s = unseen.pop()
        q = [s]
        cells = []
        for r, c in q:
            cells.append((r, c))
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    p = (r + dr, c + dc)
                    if p in unseen:
                        unseen.remove(p)
                        q.append(p)
        out.append(cells)
    return out


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    h, w = len(a), len(a[0])
    top, bot = a[0][0], a[-1][0]
    bg = Counter(v for row in a for v in row).most_common(1)[0][0]
    out = [row[:] for row in a]
    for r in range(1, h - 1):
        for c in range(w):
            if a[r][c] in (top, bot):
                out[r][c] = bg
    interior = a[1:-1]
    for color in (top, bot):
        for obj in comps([[v == color for v in row] for row in interior]):
            rs = [r for r, c in obj]
            cs = [c for r, c in obj]
            r1, r2 = min(rs), max(rs)
            c2 = max(cs)
            if color == top:
                for r, c in obj:
                    out[1 + r - r1][c] = color
            elif c2 == w - 1 and r2 - r1 + 1 >= 3:
                for c in set(cs):
                    for r in range(1 + r1, h - 1):
                        out[r][c] = color
            else:
                for r, c in obj:
                    out[h - 2 + r - r2][c] = color
    return out
