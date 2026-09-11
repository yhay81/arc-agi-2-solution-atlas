def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    colors = {(-1, -1): 3, (-1, 1): 6, (1, -1): 8, (1, 1): 7}
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 2:
                continue
            output[row][col] = 0
            for (dr, dc), color in colors.items():
                target_row, target_col = row + dr, col + dc
                if 0 <= target_row < height and 0 <= target_col < width:
                    output[target_row][target_col] = color
    return output
