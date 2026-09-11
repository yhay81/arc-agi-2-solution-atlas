def solve(grid):
    height, width = len(grid), len(grid[0])
    return [
        [
            8 if row in (0, height - 1) or col in (0, width - 1) else cell
            for col, cell in enumerate(line)
        ]
        for row, line in enumerate(grid)
    ]
