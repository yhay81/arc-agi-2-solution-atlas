def _overlay_left_flipped_right(array):
    width_all = len(array[0])
    if width_all < 3 or width_all % 2 == 0:
        return [row[:] for row in array]
    width = width_all // 2
    return [
        [
            left if left else array[r][width + 1 + width - 1 - c]
            for c, left in enumerate(row[:width])
        ]
        for r, row in enumerate(array)
    ]


def solve(grid):
    return _overlay_left_flipped_right(grid)
