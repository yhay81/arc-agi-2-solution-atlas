def solve(grid):
    return [
        [
            grid[inner_row][inner_col] if grid[row][col] else 0
            for col in range(len(grid[0]))
            for inner_col in range(len(grid[0]))
        ]
        for row in range(len(grid))
        for inner_row in range(len(grid))
    ]
