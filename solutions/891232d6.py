def points(g, color):
    return [(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v == color]


def cp(g):
    return [row[:] for row in g]


def solve(grid):
    g = grid
    out = cp(g)
    h, w = (len(g), len(g[0]))
    for r, c in points(g, 6):
        r -= 1
        while r >= 0:
            if r == 0:
                out[r][c] = 6
                break
            if g[r - 1][c] != 7:
                out[r][c] = 2
                r -= 1
                continue
            if c + 1 >= w or g[r][c + 1] == 7:
                out[r][c] = 6
                break
            out[r][c] = 4
            out[r - 1][c] = 8
            while c + 1 < w and g[r - 1][c] == 7:
                if g[r][c + 1] == 7:
                    break
                c += 1
                out[r][c] = 2
            if g[r - 1][c] == 7:
                out[r][c] = 6
                break
            out[r][c] = 3
            r -= 1
    return out
