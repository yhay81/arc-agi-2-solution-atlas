def solve(grid):
    output = [row[:] for row in grid]
    height, width = len(grid), len(grid[0])
    for row in range(height):
        for column in range(width):
            if grid[row][column] != 1:
                continue
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    r, c = row + dr, column + dc
                    if 0 <= r < height and 0 <= c < width and grid[r][c] == 0:
                        output[r][c] = 1
    return output
