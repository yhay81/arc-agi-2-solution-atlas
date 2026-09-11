def _flood_zeros_from_color_one(array):
    seeds = [(r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value == 1]
    if not seeds:
        return [row[:] for row in array]
    seen = set(seeds)
    stack = list(seeds)
    while stack:
        row, col = stack.pop()
        for next_row, next_col in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
            if (
                0 <= next_row < len(array)
                and 0 <= next_col < len(array[0])
                and ((next_row, next_col) not in seen)
                and (array[next_row][next_col] in (0, 1))
            ):
                seen.add((next_row, next_col))
                stack.append((next_row, next_col))
    if not any(array[row][col] == 0 for row, col in seen):
        return [row[:] for row in array]
    output = [row[:] for row in array]
    for row, col in seen:
        output[row][col] = 1
    return output


def solve(grid):
    return _flood_zeros_from_color_one(grid)
