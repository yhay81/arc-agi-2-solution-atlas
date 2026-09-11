def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 5:
                continue
            for target_row in range(max(0, row - 1), min(height, row + 2)):
                for target_col in range(max(0, col - 1), min(width, col + 2)):
                    if grid[target_row][target_col] == 0:
                        output[target_row][target_col] = 1
    return output
