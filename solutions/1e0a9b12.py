def _gravity_down(grid):
    output = [[0] * len(grid[0]) for _ in grid]
    for col in range(len(grid[0])):
        values = [row[col] for row in grid if row[col] != 0]
        if len(values):
            for row, value in zip(output[-len(values) :], values):
                row[col] = value
    return output


def solve(grid):
    return _gravity_down(grid)
