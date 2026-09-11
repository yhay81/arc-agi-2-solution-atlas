def _fill_same_color_bboxes(array):
    counts = {}
    for row in array:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=lambda value: (counts[value], -value))
    output = [row[:] for row in array]
    for color in counts:
        if color == background:
            continue
        positions = [
            (r, c) for r, row in enumerate(array) for c, value in enumerate(row) if value == color
        ]
        if len(positions) < 2:
            continue
        rows, cols = zip(*positions)
        top, left, bottom, right = min(rows), min(cols), max(rows), max(cols)
        for r in range(top, bottom + 1):
            for c in range(left, right + 1):
                output[r][c] = color
    return output


def solve(grid):
    return _fill_same_color_bboxes(grid)
