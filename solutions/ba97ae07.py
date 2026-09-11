def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    for row in range(1, height - 1):
        for col in range(1, width - 1):
            current = grid[row][col]
            if not current:
                continue
            start = col
            while start and grid[row][start - 1] == current:
                start -= 1
            end = col
            while end + 1 < width and grid[row][end + 1] == current:
                end += 1
            horizontal = end - start + 1
            start = row
            while start and grid[start - 1][col] == current:
                start -= 1
            end = row
            while end + 1 < height and grid[end + 1][col] == current:
                end += 1
            vertical = end - start + 1
            if (
                horizontal > vertical
                and grid[row - 1][col] == grid[row + 1][col] != 0
                and grid[row - 1][col] != current
            ):
                output[row][col] = grid[row - 1][col]
            elif vertical > horizontal:
                left = right = col
                while left and grid[row][left - 1] == current:
                    left -= 1
                while right + 1 < width and grid[row][right + 1] == current:
                    right += 1
                if (
                    left
                    and right + 1 < width
                    and grid[row][left - 1] == grid[row][right + 1] != 0
                    and grid[row][left - 1] != current
                ):
                    output[row][col] = grid[row][left - 1]
    return output
