def _mode_nested_frames(array):
    height, width = len(array), len(array[0])
    if height < 4 or width < 3:
        return [row[:] for row in array]
    interior = [v for row in array[2 : height - 1] for v in row[1 : width - 1] if v != 0]
    counts = {v: interior.count(v) for v in set(interior)}
    values = list(counts)
    if not len(values):
        return [row[:] for row in array]
    color = max(values, key=counts.get)
    output = [[0] * width for _ in range(height)]
    output[0] = array[0][:]
    output[1] = [color] * width
    output[-1] = [color] * width
    for r in range(1, height):
        output[r][0] = output[r][-1] = color
    positions = [
        (r, c) for r in range(2, height - 1) for c in range(1, width - 1) if array[r][c] == color
    ]
    if not len(positions):
        return output
    top, left = min(r for r, c in positions), min(c for r, c in positions)
    bottom, right = max(r for r, c in positions), max(c for r, c in positions)
    for c in range(left, right + 1):
        output[top][c] = output[bottom][c] = color
    for r in range(top, bottom + 1):
        output[r][left] = output[r][right] = color
    return output


def solve(grid):
    return _mode_nested_frames([row[:] for row in grid])
