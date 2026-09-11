def _roll_interior_by_header_markers(array):
    if len(array) < 3 or len(array[0]) < 3:
        return [r[:] for r in array]
    top_header = array[0][1:]
    left_header = [r[0] for r in array[1:]]
    top_background = max(set(top_header), key=top_header.count)
    left_background = max(set(left_header), key=left_header.count)
    if top_background != left_background:
        return [r[:] for r in array]
    top_markers = [i for i, v in enumerate(top_header) if v != top_background]
    left_markers = [i for i, v in enumerate(left_header) if v != left_background]
    if len(top_markers) != 1 or len(left_markers) != 1:
        return [r[:] for r in array]
    top_marker = top_header[top_markers[0]]
    left_marker = left_header[left_markers[0]]
    if top_marker != left_marker or top_marker == top_background:
        return [r[:] for r in array]
    interior = [r[1:] for r in array[1:]]
    dy, dx = left_markers[0], top_markers[0]
    return [
        row[-dx:] + row[:-dx] if dx else row[:]
        for row in (interior[-dy:] + interior[:-dy] if dy else interior)
    ]


def solve(grid):
    return _roll_interior_by_header_markers(grid)
