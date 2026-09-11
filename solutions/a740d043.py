def _crop_non_background(array):
    counts = {}
    for row in array:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=lambda value: (counts[value], -value))
    positions = [
        (r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value != background
    ]
    if not len(positions):
        return [row[:] for row in array]
    rows, cols = zip(*positions)
    top, left, bottom, right = min(rows), min(cols), max(rows), max(cols)
    return [row[left : right + 1] for row in array[top : bottom + 1]]


def solve(grid):
    output = _crop_non_background(grid)
    color_map = {3: 3, 1: 0, 2: 2, 5: 5, 6: 6}
    source = [row[:] for row in output]
    for old, new in color_map.items():
        for r, row in enumerate(source):
            for c, value in enumerate(row):
                if value == old:
                    output[r][c] = new
    return output
