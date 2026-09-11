def _extend(grid):
    h, w = len(grid), len(grid[0])
    counts = {}
    positions = {}
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            if v:
                counts[v] = counts.get(v, 0) + 1
                positions.setdefault(v, []).append((r, c))
    if len(counts) != 2:
        return [row[:] for row in grid]
    marker, body = sorted(counts, key=counts.get)
    if counts[marker] != 1:
        return [row[:] for row in grid]
    mr, mc = positions[marker][0]
    bp = positions[body]
    top, bottom = min(r for r, c in bp), max(r for r, c in bp)
    left, right = min(c for r, c in bp), max(c for r, c in bp)
    sides = []
    if mr <= top and top - mr <= 1:
        sides.append("top")
    if mr >= bottom and mr - bottom <= 1:
        sides.append("bottom")
    if mc <= left and left - mc <= 1:
        sides.append("left")
    if mc >= right and mc - right <= 1:
        sides.append("right")
    if len(sides) != 1:
        return [row[:] for row in grid]
    out = [row[:] for row in grid]
    if sides[0] == "top":
        for r in range(bottom + 1, h):
            out[r][mc] = marker
    elif sides[0] == "bottom":
        for r in range(top):
            out[r][mc] = marker
    elif sides[0] == "left":
        for c in range(right + 1, w):
            out[mr][c] = marker
    else:
        for c in range(left):
            out[mr][c] = marker
    return out


def solve(grid):
    return _extend(grid)
