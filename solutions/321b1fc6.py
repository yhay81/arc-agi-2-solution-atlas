def solve(grid):
    height, width = len(grid), len(grid[0])
    colors = {value for row in grid for value in row if value != 0}
    candidates = []
    for color in colors:
        seen = set()
        components = []
        for row in range(height):
            for col in range(width):
                if grid[row][col] != color or (row, col) in seen:
                    continue
                stack = [(row, col)]
                seen.add((row, col))
                cells = []
                while stack:
                    r, c = stack.pop()
                    cells.append((r, c))
                    for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if (
                            0 <= rr < height
                            and 0 <= cc < width
                            and grid[rr][cc] == color
                            and (rr, cc) not in seen
                        ):
                            seen.add((rr, cc))
                            stack.append((rr, cc))
                components.append(cells)
        if len(components) < 2:
            continue
        shapes, boxes = [], []
        for cells in components:
            top, left = min(r for r, _ in cells), min(c for _, c in cells)
            bottom, right = max(r for r, _ in cells), max(c for _, c in cells)
            shapes.append(tuple(sorted((r - top, c - left) for r, c in cells)))
            boxes.append((top, bottom, left, right))
        if len(set(shapes)) != 1:
            continue
        template_cells = [
            (r, c)
            for r in range(height)
            for c in range(width)
            if grid[r][c] != 0 and grid[r][c] != color
        ]
        if not template_cells:
            continue
        top, left = min(r for r, _ in template_cells), min(c for _, c in template_cells)
        bottom, right = max(r for r, _ in template_cells), max(c for _, c in template_cells)
        template_shape = tuple(sorted((r - top, c - left) for r, c in template_cells))
        if template_shape == shapes[0]:
            candidates.append((boxes, (top, bottom, left, right)))
    if len(candidates) != 1:
        return [row[:] for row in grid]
    boxes, (top, bottom, left, right) = candidates[0]
    template = [row[left : right + 1] for row in grid[top : bottom + 1]]
    output = [[0] * width for _ in range(height)]
    for box_top, box_bottom, box_left, box_right in boxes:
        for row, line in enumerate(template):
            for col, value in enumerate(line):
                output[box_top + row][box_left + col] = value
    return output
