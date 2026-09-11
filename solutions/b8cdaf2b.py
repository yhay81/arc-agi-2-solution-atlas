def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    non = [r for r, row in enumerate(a) if any(row)]
    if len(non) < 2:
        return [r[:] for r in a]
    u, l = non[-2:]
    center = w // 2
    color = a[l][center]
    if not color:
        return [r[:] for r in a]
    pos = [c for c, v in enumerate(a[l]) if v == color]
    left, right = pos[0], pos[-1]
    while left < center and a[l][left] == color:
        left += 1
    while right > center and a[l][right] == color:
        right -= 1
    if a[l][left] != color:
        left = max(0, left - 1)
    if a[l][right] != color:
        right = min(w - 1, right + 1)
    up = [c for c, v in enumerate(a[u]) if v]
    if up:
        left, right = up[0], up[-1]
    dist = min(left, w - 1 - right)
    if dist <= 0:
        return [r[:] for r in a]
    out = [r[:] for r in a]
    empt = [r for r in range(u - 1, -1, -1) if not any(a[r])][:dist]
    for d, r in enumerate(empt, 1):
        if 0 <= left - d < w:
            out[r][left - d] = color
        if 0 <= right + d < w:
            out[r][right + d] = color
    return out
