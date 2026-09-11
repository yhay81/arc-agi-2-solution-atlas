def solve(grid):
    a = grid
    a = [row[:] for row in a]
    ps = sorted([(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v == 1])
    dy = (ps[-1][0] > ps[0][0]) - (ps[-1][0] < ps[0][0])
    dx = (ps[-1][1] > ps[0][1]) - (ps[-1][1] < ps[0][1])
    if not (dy and dx):
        raise ValueError("task assumptions are not satisfied")
    out = [row[:] for row in a]
    for p, direction in [(ps[0], (-dy, -dx)), (ps[-1], (dy, dx))]:
        y, x = p
        sy, sx = direction
        seen = set()
        for _ in range(len(a) * len(a[0]) * 4):
            state = (y, x, sy, sx)
            if state in seen:
                break
            seen.add(state)
            ny, nx = (y + sy, x + sx)
            if not (0 <= ny < len(a) and 0 <= nx < len(a[0])):
                break
            if a[ny][nx] == 2:
                vertical = sum(a[rr][nx] == 2 for rr in range(len(a))) > sum(
                    a[ny][cc] == 2 for cc in range(len(a[0]))
                )
                if vertical:
                    sx = -sx
                else:
                    sy = -sy
                ny, nx = (y + sy, x + sx)
            if not (0 <= ny < len(a) and 0 <= nx < len(a[0])):
                break
            out[ny][nx] = 1
            y, x = (ny, nx)
    return out
