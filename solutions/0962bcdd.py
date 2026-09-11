def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    offsets = [
        (-2, -2, "c"),
        (-2, 0, "a"),
        (-2, 2, "c"),
        (-1, -1, "c"),
        (-1, 0, "a"),
        (-1, 1, "c"),
        (0, -2, "a"),
        (0, -1, "a"),
        (0, 0, "c"),
        (0, 1, "a"),
        (0, 2, "a"),
        (1, -1, "c"),
        (1, 0, "a"),
        (1, 1, "c"),
        (2, -2, "c"),
        (2, 0, "a"),
        (2, 2, "c"),
    ]
    for r in range(1, h - 1):
        for c in range(1, w - 1):
            center = grid[r][c]
            arms = [grid[r - 1][c], grid[r + 1][c], grid[r][c - 1], grid[r][c + 1]]
            if not center or any(v == 0 for v in arms) or len(set(arms)) != 1 or arms[0] == center:
                continue
            for dr, dc, kind in offsets:
                rr, cc = r + dr, c + dc
                if 0 <= rr < h and 0 <= cc < w:
                    out[rr][cc] = center if kind == "c" else arms[0]
    return out
