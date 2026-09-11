def solve(grid):
    a = grid
    a = [row[:] for row in a]
    bg = 7
    lamp = 6
    h, w = len(a), len(a[0])
    out = [row[:] for row in a]
    fire = []

    def bar(r):
        return next((v for v in a[r][2:] if v != bg), None)

    for r in range(1, h - 1, 2):
        if bar(r - 1) == bar(r + 1):
            fire.append(r)
            out[r][0] = bg
    obstacles = out.copy()
    ends = []
    for start in fire:
        r, c = (start, 0)
        dr, dc = (0, 1)
        seen = set()
        while (r, c, dr, dc) not in seen:
            seen.add((r, c, dr, dc))
            nr, nc = (r + dr, c + dc)
            if not (0 <= nr < h and 0 <= nc < w):
                break
            if obstacles[nr][nc] == bg:
                r, c = (nr, nc)
                continue
            opts = []
            for dy, dx in [(-dc, dr), (dc, -dr)]:
                y, x = (r + dy, c + dx)
                if 0 <= y < h and 0 <= x < w and obstacles[y][x] == bg:
                    opts.append((dy, dx))
            if len(opts) != 1:
                break
            dy, dx = opts[0]
            if (dy, dx) == (0, -1) and obstacles[r][0] == lamp:
                break
            dr, dc = (dy, dx)
        ends.append((r, c))
    for r, c in ends:
        out[r][c] = lamp
    return out
