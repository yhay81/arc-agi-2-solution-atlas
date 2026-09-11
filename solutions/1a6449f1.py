def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    candidates = []
    for top in range(h - 2):
        for left in range(w - 2):
            color = g[top][left]
            if color == 0:
                continue
            for right in range(left + 2, w):
                if not all(v == color for v in g[top][left : right + 1]):
                    break
                for bottom in range(top + 2, h):
                    if not all(g[r][left] == g[r][right] == color for r in range(top, bottom + 1)):
                        continue
                    if all(v == color for v in g[bottom][left : right + 1]):
                        candidates.append(
                            ((bottom - top + 1) * (right - left + 1), top, bottom, left, right)
                        )
    if not candidates:
        raise ValueError("No frame")
    area, top, bottom, left, right = max(candidates)
    return [row[left + 1 : right] for row in g[top + 1 : bottom]]
