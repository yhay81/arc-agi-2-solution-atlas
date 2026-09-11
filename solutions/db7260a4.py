def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    out = copy(g)
    h, w = (len(g), len(g[0]))
    col = next((c for c, v in enumerate(g[0]) if v == 1))
    out[0][col] = 0
    bands = []
    start = None
    for r, row in enumerate(g + [[0] * w]):
        if 2 in row and start is None:
            start = r
        if 2 not in row and start is not None:
            bands.append((start, r - 1))
            start = None
    for top, bottom in bands:
        if not any(g[r][col] == 2 for r in range(top, bottom + 1)):
            continue
        hit = next(r for r in range(top, bottom + 1) if g[r][col] == 2)
        if hit == top:
            continue
        seen = {(hit - 1, col)}
        q = list(seen)
        while q:
            a, b = q.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                p = (a + dr, b + dc)
                if (
                    top <= p[0] <= bottom
                    and 0 <= p[1] < w
                    and (p not in seen)
                    and (g[p[0]][p[1]] == 0)
                ):
                    seen.add(p)
                    q.append(p)
        exits = [c for r, c in seen if r == bottom]
        if not exits and (not any((c in (0, w - 1) for r, c in seen))):
            for r, c in seen:
                out[r][c] = 1
            return out
        if exits:
            col = min(exits, key=lambda c: abs(c - col))
    out[-1] = [1] * w
    return out
