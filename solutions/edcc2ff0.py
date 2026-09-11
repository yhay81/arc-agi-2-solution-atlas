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
    out = [row[:] for row in a]
    h, w = (len(a), len(a[0]))
    top = next((r for r, row in enumerate(a) if 0 not in row))
    bg = Counter(v for row in a[top:] for v in row).most_common(1)[0][0]
    legend = [(r, a[r][0]) for r in range(top) if a[r][0] != 0]
    allowed = {v for r, v in legend}
    counts = Counter((v for v, pts in cc(a[top:], bg)))
    for r, v in legend:
        for c in range(w):
            out[r][c] = v if c < counts[v] else 0
    for r in range(top, h):
        for c in range(w):
            if a[r][c] not in allowed:
                out[r][c] = bg
    return out
