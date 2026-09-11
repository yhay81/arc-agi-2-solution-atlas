from collections import Counter


def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    border = g[0][0]
    counts = Counter(v for row in g for v in row)
    background = max((v for v in counts if v != border), key=lambda v: counts[v])
    marker = next((v for v in counts if v not in (border, background)), border)
    dividers = [c for c in range(w) if all(g[r][c] == border for r in range(h))]
    if len(dividers) < 3:
        raise ValueError("Animation frames not found")
    frame_w = dividers[1] - dividers[0] + 1
    states = []
    for left, right in zip(dividers[:-1], dividers[1:]):
        pts = {
            (r, c - left)
            for r in range(1, h - 1)
            for c in range(left + 1, right)
            if g[r][c] == marker
        }
        if not pts:
            raise ValueError("Empty animation frame")
        states.append(pts)
    anchors = [(min((r for r, c in s)), min((c for r, c in s))) for s in states]
    dr = anchors[-1][0] - anchors[-2][0]
    dc = anchors[-1][1] - anchors[-2][1]
    if marker == border and dr > 0:
        dr += 1
    last = states[-1]
    ar, ac = anchors[-1]
    shape = {(r - ar, c - ac) for r, c in last}
    nr, nc = (ar + dr, ac + dc)
    out = [[background] * frame_w for _ in range(h)]
    for c in range(frame_w):
        out[0][c] = out[h - 1][c] = border
    for r in range(h):
        out[r][0] = out[r][frame_w - 1] = border
    for r, c in shape:
        out[nr + r][nc + c] = marker
    return out
