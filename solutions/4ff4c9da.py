def solve(grid):
    height, width = len(grid), len(grid[0])
    row_separators = [r for r in range(height) if len(set(grid[r])) == 1 and grid[r][0] != 0]
    col_separators = [
        c for c in range(width) if len({grid[r][c] for r in range(height)}) == 1 and grid[0][c] != 0
    ]
    if not row_separators or not col_separators or not any(8 in row for row in grid):
        return [row[:] for row in grid]
    separator_colors = {grid[r][0] for r in row_separators}
    row_edges = [-1, *row_separators, height]
    col_edges = [-1, *col_separators, width]
    cells = []
    for top, bottom in zip(row_edges, row_edges[1:]):
        for left, right in zip(col_edges, col_edges[1:]):
            region = [row[left + 1 : right] for row in grid[top + 1 : bottom]]
            if region:
                cells.append((top + 1, left + 1, bottom, right, region))

    def mask_signature(mask):
        points = [(r, c) for r, row in enumerate(mask) for c, value in enumerate(row) if value]
        if not points:
            return ()
        top = min(r for r, _ in points)
        left = min(c for _, c in points)
        bottom = max(r for r, _ in points)
        right = max(c for _, c in points)
        return tuple(
            tuple(int(mask[r][c]) for c in range(left, right + 1)) for r in range(top, bottom + 1)
        )

    prototypes = []
    for _top, _left, _bottom, _right, region in cells:
        mask = [[value == 8 for value in row] for row in region]
        if any(any(row) for row in mask):
            prototypes.append((len(region), len(region[0]), mask_signature(mask)))
    if not prototypes:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for top, left, bottom, right, region in cells:
        for shape_h, shape_w, prototype in prototypes:
            if (len(region), len(region[0])) != (shape_h, shape_w):
                continue
            for color in {value for row in region for value in row}:
                if color in (0, 8) or color in separator_colors:
                    continue
                mask = [[value == color for value in row] for row in region]
                if mask_signature(mask) != prototype:
                    continue
                for r in range(len(region)):
                    for c in range(len(region[0])):
                        if region[r][c] == color:
                            output[top + r][left + c] = 8
    return output
