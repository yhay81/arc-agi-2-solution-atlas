def _remove_singletons(grid):
    output = [row[:] for row in grid]
    for row, line in enumerate(grid):
        for col, value in enumerate(line):
            if (
                value
                and sum(
                    grid[r][c] == value
                    for r in range(max(0, row - 1), min(len(grid), row + 2))
                    for c in range(max(0, col - 1), min(len(line), col + 2))
                )
                == 1
            ):
                output[row][col] = 0
    return output


def solve(grid):
    return _remove_singletons(grid)
