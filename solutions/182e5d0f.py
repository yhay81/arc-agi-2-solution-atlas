def solve(grid):
    height, width = len(grid), len(grid[0])
    background, object_color, cell_color = 7, 3, 5
    unseen = {(r, c) for r in range(height) for c in range(width) if grid[r][c] != background}
    objects = []
    while unseen:
        start = unseen.pop()
        cells = [start]
        for row, col in cells:
            for rr, cc in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if (rr, cc) in unseen and grid[rr][cc] == grid[start[0]][start[1]]:
                    unseen.remove((rr, cc))
                    cells.append((rr, cc))
        objects.append(cells)
    lookup = {(r, c): cells for cells in objects for r, c in cells}
    output = [row[:] for row in grid]
    for cell_row in range(height):
        for cell_col in range(width):
            if grid[cell_row][cell_col] != cell_color:
                continue
            touching = [
                lookup.get((rr, cc))
                for rr, cc in (
                    (cell_row - 1, cell_col),
                    (cell_row + 1, cell_col),
                    (cell_row, cell_col - 1),
                    (cell_row, cell_col + 1),
                )
            ]
            touching = [cells for cells in touching if cells]
            if not touching:
                continue
            component = touching[0]
            anchor = None
            zero_positions = []
            for row, col in component:
                neighbours = [
                    (row + dr, col + dc)
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))
                    if 0 <= row + dr < height and 0 <= col + dc < width
                ]
                zeros = [(r, c) for r, c in neighbours if output[r][c] == 0]
                if len(zeros) == 2:
                    anchor, zero_positions = (row, col), zeros
                    break
            if anchor is None:
                continue
            for row, col in component:
                if (row, col) != anchor:
                    output[row][col] = background
            output[cell_row][cell_col] = background
            horizontal = zero_positions[0][0] == zero_positions[1][0]
            row, col = anchor
            if horizontal:
                for delta in (-1, 1):
                    rr = row + delta
                    if 0 <= rr < height and output[rr][col] in (background, 0):
                        output[rr][col] = cell_color
                        break
            else:
                for delta in (-1, 1):
                    cc = col + delta
                    if 0 <= cc < width and output[row][cc] in (background, 0):
                        output[row][cc] = cell_color
                        break
    return output
