def _project(grid):
    h, w = len(grid), len(grid[0])
    colors = {v for row in grid for v in row}
    candidates = [
        v
        for v in colors
        if v
        and sum(x == v for x in grid[-1]) >= 2
        and all(grid[r][c] != v for r in range(h - 1) for c in range(w))
    ]
    if len(candidates) != 1:
        return [row[:] for row in grid]
    ray = candidates[0]
    blockers = colors - {0, ray}
    if not blockers:
        return [row[:] for row in grid]
    out = [row[:] for row in grid]
    bent = False
    for start in [c for c, v in enumerate(grid[-1]) if v == ray]:
        col, active = start, True
        for r in range(h - 2, -1, -1):
            while grid[r][col] in blockers:
                nc = col + 1
                if nc >= w or out[r + 1][nc] not in (0, ray):
                    active = False
                    break
                out[r + 1][nc] = ray
                col = nc
                bent = True
            if not active:
                break
            if out[r][col] not in (0, ray):
                active = False
                break
            out[r][col] = ray
    return out if bent else [row[:] for row in grid]


def solve(grid):
    return _project(grid)
