def _mark_count_difference(grid):
    output = [row[:] for row in grid]
    difference = max(
        0, sum(v == 8 for row in grid for v in row) - sum(v == 2 for row in grid for v in row)
    )
    if difference:
        for row in output[-difference:]:
            row[-2] = 5
    return output


def solve(grid):
    return _mark_count_difference(grid)
