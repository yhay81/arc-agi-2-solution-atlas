def _recolor_plus_shapes(array, foreground=4, replacement=8):
    centers: list[tuple[int, int]] = []
    for row in range(1, len(array) - 1):
        for col in range(1, len(array[0]) - 1):
            if array[row][col] != foreground:
                continue
            if all(
                (
                    array[row + dr][col + dc] == foreground
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))
                )
            ):
                centers.append((row, col))
    output = [row[:] for row in array]
    for row, col in centers:
        output[row][col] = replacement
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            output[row + dr][col + dc] = replacement
    return output


def solve(grid):
    return _recolor_plus_shapes(grid, 4, 8)
