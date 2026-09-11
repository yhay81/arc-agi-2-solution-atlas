def copy(g):
    return [r[:] for r in g]


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    out = copy(g)
    h, w = (len(g), len(g[0]))
    used = set()
    for r, row in enumerate(g):
        for c, v in enumerate(row):
            if v != 1:
                continue
            options = []
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                a, b = (r + dr, c + dc)
                if not (0 <= a < h and 0 <= b < w) or g[a][b] != 6:
                    continue
                for sign in (-1, 1):
                    x, y = (r + sign * dr, c + sign * dc)
                    while 0 <= x < h and 0 <= y < w:
                        if g[x][y] == 7:
                            options.append((a, b, sign))
                            break
                        x += sign * dr
                        y += sign * dc
            if len(options) != 1:
                raise ValueError("adjacent domino and orange direction are not unique")
            a, b, sign = options[0]
            out[r][c] = 1 if sign == 1 else 6
            out[a][b] = 6 if sign == 1 else 1
    return out
