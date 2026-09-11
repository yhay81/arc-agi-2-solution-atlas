def _fundamental_tile(array):
    height, width = len(array), len(array[0])
    for rows in range(1, height + 1):
        for cols in range(1, width + 1):
            if height % rows or width % cols:
                continue
            if all(
                array[r][c] == array[r % rows][c % cols]
                for r in range(height)
                for c in range(width)
            ):
                return [row[:cols] for row in array[:rows]]
    return [row[:] for row in array]


def solve(grid):
    return _fundamental_tile(grid)
