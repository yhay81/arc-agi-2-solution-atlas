def _tile_left_prefix_horizontally(array):
    occupied = [(r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v != 0]
    if not occupied:
        return [row[:] for row in array]
    last_occupied_col = max(c for _, c in occupied)
    if last_occupied_col >= len(array[0]) - 1:
        return [row[:] for row in array]
    periods = [
        period
        for period in range(1, last_occupied_col + 2)
        if all(
            all(array[r][col] == array[r][col % period] for r in range(len(array)))
            for col in range(last_occupied_col + 1)
        )
    ]
    if not periods:
        return [row[:] for row in array]
    period = periods[0]
    if last_occupied_col < period:
        return [row[:] for row in array]
    return [[array[r][col % period] for col in range(len(array[0]))] for r in range(len(array))]


def solve(grid):
    return _tile_left_prefix_horizontally(grid)
