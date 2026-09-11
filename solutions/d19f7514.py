def solve(grid):
    if len(grid) % 2:
        raise ValueError("Expected equally sized upper and lower panels")
    half = len(grid) // 2
    return [
        [0 if grid[r][c] == grid[r + half][c] == 0 else 4 for c in range(len(grid[0]))]
        for r in range(half)
    ]
