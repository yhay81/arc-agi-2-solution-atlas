def solve(grid):
    h, w = len(grid), len(grid[0])
    return [
        [grid[inner_r][inner_c] if grid[r][c] else 0 for c in range(w) for inner_c in range(w)]
        for r in range(h)
        for inner_r in range(h)
    ]
