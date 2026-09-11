def solve(grid):
    a = grid
    a = [row[:] for row in a]
    h, w = len(a), len(a[0])
    t = {
        2: [[4, 4, 4, 4], [4, 0, 0, 4], [4, 0, 0, 4], [4, 4, 4, 4]],
        3: [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]],
        5: [[6, 6, 0, 0], [6, 6, 0, 0], [0, 0, 6, 6], [0, 0, 6, 6]],
        8: [[7, 0, 0, 7], [0, 7, 7, 0], [0, 7, 7, 0], [7, 0, 0, 7]],
    }
    b = [r[:] for r in a]
    for color, z in t.items():
        for y in range(h - 4):
            for x in range(w - 4):
                if (
                    a[y + 4][x + 4] == color
                    and all(
                        a[y + i][x + j] == z[i][j] for i in range(4) for j in range(4) if z[i][j]
                    )
                    and all(
                        a[y + i][x + j] in (0, color)
                        for i in range(4)
                        for j in range(4)
                        if not z[i][j]
                    )
                ):
                    for i in range(4):
                        for j in range(4):
                            if z[i][j]:
                                b[y + i][x + j] = 0
                    b[y + 4][x + 4] = 0
    out = [[0] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            if b[y][x] and b[y][x] in t:
                for i in range(min(4, h - y)):
                    for j in range(min(4, w - x)):
                        out[y + i][x + j] = t[b[y][x]][i][j]
    return out
