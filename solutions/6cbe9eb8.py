def solve(grid):
    height, width = len(grid), len(grid[0])
    objects = []
    for color in {value for row in grid for value in row}:
        cells = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == color]
        top, bottom = min(r for r, _ in cells), max(r for r, _ in cells)
        left, right = min(c for _, c in cells), max(c for _, c in cells)
        box_height, box_width = bottom - top + 1, right - left + 1
        border = sum(r in (top, bottom) or c in (left, right) for r, c in cells)
        perimeter = 2 * box_height + 2 * box_width - 4
        if len(cells) == box_height * box_width:
            kind = "solid"
        elif min(box_height, box_width) >= 3 and border == len(cells) and len(cells) <= perimeter:
            kind = "frame"
        else:
            continue
        objects.append((box_height * box_width, color, box_height, box_width, kind))
    objects.sort(reverse=True)
    if len(objects) < 2:
        return [row[:] for row in grid]
    canvas_height, canvas_width = objects[0][2:4]
    output = [[0] * canvas_width for _ in range(canvas_height)]
    parent_top = parent_left = parent_height = 0
    parent_kind = ""
    for index, (_, color, box_height, box_width, kind) in enumerate(objects):
        if index == 0:
            top = left = 0
        elif parent_kind == "solid":
            top, left = parent_top + parent_height - box_height, parent_left
        else:
            top, left = parent_top + parent_height - box_height - 1, parent_left + 1
        if (
            top < 0
            or left < 0
            or top + box_height > canvas_height
            or left + box_width > canvas_width
        ):
            return [row[:] for row in grid]
        for r in range(box_height):
            for c in range(box_width):
                if kind == "solid" or r in (0, box_height - 1) or c in (0, box_width - 1):
                    output[top + r][left + c] = color
        parent_top, parent_left, parent_height, parent_kind = top, left, box_height, kind
    return output
