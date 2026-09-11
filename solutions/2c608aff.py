def _project_markers_to_solid_rectangle(array):
    values = {v for row in array for v in row}
    background = max(values, key=lambda v: sum(x == v for row in array for x in row))
    rectangles: list[tuple[int, int, int, int, int]] = []
    for value in values:
        color = int(value)
        if color == background:
            continue
        cells = [(r, c) for r, row in enumerate(array) for c, x in enumerate(row) if x == color]
        top, left = min(r for r, _ in cells), min(c for _, c in cells)
        bottom, right = max(r for r, _ in cells), max(c for _, c in cells)
        if len(cells) >= 4 and len(cells) == (bottom - top + 1) * (right - left + 1):
            rectangles.append((color, int(top), int(bottom), int(left), int(right)))
    if len(rectangles) != 1:
        return [row[:] for row in array]
    rectangle_color, top, bottom, left, right = rectangles[0]
    output = [row[:] for row in array]
    changed = False
    for row in range(len(array)):
        for col in range(len(array[0])):
            if array[row][col] in (background, rectangle_color):
                continue
            ray: list[tuple[int, int]] = []
            if top <= row <= bottom and col < left:
                ray = [(row, next_col) for next_col in range(col + 1, left)]
            elif top <= row <= bottom and col > right:
                ray = [(row, next_col) for next_col in range(right + 1, col)]
            elif left <= col <= right and row < top:
                ray = [(next_row, col) for next_row in range(row + 1, top)]
            elif left <= col <= right and row > bottom:
                ray = [(next_row, col) for next_row in range(bottom + 1, row)]
            for ray_row, ray_col in ray:
                if output[ray_row][ray_col] != background:
                    return [r[:] for r in array]
                output[ray_row][ray_col] = array[row][col]
                changed = True
    return output if changed else [row[:] for row in array]


def solve(grid):
    return _project_markers_to_solid_rectangle([row[:] for row in grid])
