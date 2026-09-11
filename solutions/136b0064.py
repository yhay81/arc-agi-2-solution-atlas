def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    mid = next(c for c in range(w) if len({row[c] for row in g}) == 1 and g[0][c] != 0)
    out = [row[mid + 1 :] for row in g]
    start = [(r, c) for r, row in enumerate(out) for c, v in enumerate(row) if v]
    r, c = start[0]
    r += 1
    commands = {
        (1, 0, 1, 1, 0, 1, 1, 1, 1): (-1, 1),
        (1, 1, 0, 1, 0, 1, 0, 1, 0): (2, 1),
        (1, 0, 1, 0, 1, 0, 0, 1, 0): (0, 2),
        (1, 1, 1, 0, 1, 0, 1, 0, 1): (-3, 1),
    }
    for left in range(0, mid, 4):
        for top in range(0, h, 4):
            tile = [row[left : left + 3] for row in g[top : top + 3]]
            key = tuple(int(v != 0) for row in tile for v in row)
            color = next(v for row in tile for v in row if v)
            dx, dh = commands[key]
            if dx:
                for b in range(min(c, c + dx), max(c, c + dx) + 1):
                    out[r][b] = color
                c += dx
                r += 1
            else:
                for a in range(r, r + dh):
                    out[a][c] = color
                r += dh
    return out
