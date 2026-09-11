def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = [r[:] for r in g]
    h, w = (len(g), len(g[0]))
    rectangles = []
    used = set()
    for top in range(h - 1):
        for bottom in range(top + 1, h):
            columns = [all(g[r][c] == 0 for r in range(top, bottom + 1)) for c in range(w)]
            for left in range(w - 1):
                if not columns[left]:
                    continue
                for right in range(left + 1, w):
                    if not columns[right]:
                        break
                    rectangles.append(
                        (-(bottom - top + 1) * (right - left + 1), top, left, bottom, right)
                    )
    for _, top, left, bottom, right in sorted(rectangles):
        cells = {(r, c) for r in range(top, bottom + 1) for c in range(left, right + 1)}
        if cells & used:
            continue
        used.update(cells)
        for r, c in cells:
            out[r][c] = 2
    return out
