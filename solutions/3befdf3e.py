def solve(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0 or (row, col) in seen:
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
                        and grid[rr][cc] != 0
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        stack.append((rr, cc))
            components.append(cells)
    output = [row[:] for row in grid]
    for cells in components:
        top, left = min(r for r, _ in cells), min(c for _, c in cells)
        bottom, right = max(r for r, _ in cells), max(c for _, c in cells)
        side = bottom - top + 1
        if side != right - left + 1 or side < 3 or len(cells) != side * side:
            continue
        border = (
            [grid[top][c] for c in range(left, right + 1)]
            + [grid[bottom][c] for c in range(left, right + 1)]
            + [grid[r][left] for r in range(top + 1, bottom)]
            + [grid[r][right] for r in range(top + 1, bottom)]
        )
        if len(set(border)) != 1:
            continue
        border_color = border[0]
        inner_values = {grid[r][c] for r in range(top + 1, bottom) for c in range(left + 1, right)}
        if len(inner_values) != 1:
            continue
        inner_color = next(iter(inner_values))
        if inner_color == border_color:
            continue
        size = 2 * side if side % 2 == 0 else 2 * side - 1
        top_out, left_out = top - side // 2, left - side // 2
        bottom_out, right_out = top_out + size, left_out + size
        if top_out < 0 or left_out < 0 or bottom_out > height or right_out > width:
            continue
        for r, c in cells:
            output[r][c] = 0
        corner = side // 2
        for r in range(top_out, bottom_out):
            for c in range(left_out, right_out):
                edge_row = min(r - top_out, bottom_out - 1 - r)
                edge_col = min(c - left_out, right_out - 1 - c)
                if edge_row < corner and edge_col < corner:
                    continue
                layer = min(edge_row, edge_col) // corner
                output[r][c] = border_color if layer % 2 == 0 else inner_color
        center_size = 2 if side % 2 == 0 else 1
        center_top = top_out + (size - center_size) // 2
        center_left = left_out + (size - center_size) // 2
        for r in range(center_top, center_top + center_size):
            for c in range(center_left, center_left + center_size):
                output[r][c] = border_color
    return output
