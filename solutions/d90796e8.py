def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 2:
                continue
            neighbors = [
                (next_row, next_col)
                for next_row, next_col in (
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                )
                if 0 <= next_row < height
                and 0 <= next_col < width
                and grid[next_row][next_col] == 3
            ]
            if neighbors:
                output[row][col] = 0
                for next_row, next_col in neighbors:
                    output[next_row][next_col] = 8
    return output
