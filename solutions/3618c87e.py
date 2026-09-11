def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 1:
                continue
            directions = [
                (dr, dc)
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))
                if 0 <= row + dr < height
                and 0 <= col + dc < width
                and grid[row + dr][col + dc] == 5
            ]
            if len(directions) != 1:
                continue
            dr, dc = directions[0]
            target_row, target_col = row + dr, col + dc
            while (
                0 <= target_row + dr < height
                and 0 <= target_col + dc < width
                and grid[target_row + dr][target_col + dc] == 5
            ):
                target_row += dr
                target_col += dc
            output[row][col] = 0
            output[target_row][target_col] = 1
    return output
