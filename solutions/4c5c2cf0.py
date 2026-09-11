def _reflect(grid):
    h, w = len(grid), len(grid[0]) if grid else 0
    colors = sorted({v for row in grid for v in row if v})
    if len(colors) != 2:
        return [r[:] for r in grid]
    candidates = []
    for color in colors:
        cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == color]
        top, left = min(r for r, c in cells), min(c for r, c in cells)
        bottom, right = max(r for r, c in cells), max(c for r, c in cells)
        shape = [
            [grid[r][c] == color for c in range(left, right + 1)] for r in range(top, bottom + 1)
        ]
        if shape == shape[::-1] and all(
            a == b for a, b in zip(shape, map(list, zip(*shape[::-1])))
        ):
            candidates.append(color)
    if len(candidates) != 1:
        return [r[:] for r in grid]
    marker = candidates[0]
    payload = next(c for c in colors if c != marker)
    cells = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == marker]
    cr = min(r for r, c in cells) + max(r for r, c in cells)
    cc = min(c for r, c in cells) + max(c for r, c in cells)
    out = [r[:] for r in grid]
    for r in range(h):
        for c in range(w):
            if grid[r][c] != payload:
                continue
            for rr, rc in ((r, c), (cr - r, c), (r, cc - c), (cr - r, cc - c)):
                if not (0 <= rr < h and 0 <= rc < w and out[rr][rc] in (0, payload)):
                    return [x[:] for x in grid]
                out[rr][rc] = payload
    return out


def solve(grid):
    return _reflect(grid)
