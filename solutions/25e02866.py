from collections import Counter


def cc(a, bg=0, colorwise=True):
    h, w = (len(a), len(a[0]))
    seen = set()
    out = []
    for r in range(h):
        for c in range(w):
            if a[r][c] == bg or (r, c) in seen:
                continue
            color = a[r][c]
            q = [(r, c)]
            seen.add((r, c))
            cells = []
            for rr, cc_ in q:
                cells.append((rr, cc_))
                for nr, nc in [(rr - 1, cc_), (rr + 1, cc_), (rr, cc_ - 1), (rr, cc_ + 1)]:
                    if (
                        0 <= nr < h
                        and 0 <= nc < w
                        and ((nr, nc) not in seen)
                        and (a[nr][nc] != bg)
                        and (not colorwise or a[nr][nc] == color)
                    ):
                        seen.add((nr, nc))
                        q.append((nr, nc))
            out.append((color, cells))
    return out


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    bg = Counter(v for row in a for v in row).most_common(1)[0][0]
    blocks = []
    for v, pts in cc(a, bg, False):
        r0 = min((r for r, c in pts))
        r1 = max((r for r, c in pts))
        c0 = min((c for r, c in pts))
        c1 = max((c for r, c in pts))
        blocks.append([row[c0 : c1 + 1] for row in a[r0 : r1 + 1]])
    n = len(blocks[0])
    base = Counter(v for b in blocks for row in b for v in row).most_common(1)[0][0]
    out = [[base] * n for _ in range(n)]
    for b in blocks:
        if not (len(b) == n and len(b[0]) == n):
            raise ValueError("task assumptions are not satisfied")
        for r, row in enumerate(b):
            for c, v in enumerate(row):
                if v != base:
                    if out[r][c] not in (base, v):
                        raise ValueError("task assumptions are not satisfied")
                    out[r][c] = v
    return out
