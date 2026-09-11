def _spans(length, separators):
    boundaries = [-1, *sorted(separators), length]
    return [
        (first + 1, second)
        for first, second in zip(boundaries, boundaries[1:])
        if first + 1 < second
    ]


def solve(grid):
    height, width = len(grid), len(grid[0])
    separator_rows = {row for row, values in enumerate(grid) if all(value == 5 for value in values)}
    separator_cols = {
        col for col in range(width) if all(grid[row][col] == 5 for row in range(height))
    }
    output = [row[:] for row in grid]
    color_map = {1: 6, 2: 7, 3: 8, 4: 9}
    for top, bottom in _spans(height, separator_rows):
        for left, right in _spans(width, separator_cols):
            markers = {
                grid[row][col]
                for row in range(top, bottom)
                for col in range(left, right)
                if grid[row][col] in color_map
            }
            if len(markers) != 1:
                continue
            color = color_map[markers.pop()]
            for row in range(top, bottom):
                for col in range(left, right):
                    output[row][col] = color
    return output
