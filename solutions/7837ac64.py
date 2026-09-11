def _bounding_crop(array, mask):
    positions = [(r, c) for r, row in enumerate(mask) for c, v in enumerate(row) if v]
    if not len(positions):
        return [row[:] for row in array]
    top = min(r for r, _ in positions)
    left = min(c for _, c in positions)
    bottom = max(r for r, _ in positions)
    right = max(c for _, c in positions)
    return [row[left : right + 1] for row in array[top : bottom + 1]]


def _decode_colored_lattice_cells(array):
    nonzero = [v for row in array for v in row if v != 0]
    if not len(nonzero):
        return [row[:] for row in array]
    colors = set(nonzero)
    grid_color = max(colors, key=nonzero.count)
    row_lines = [r for r, row in enumerate(array) if all(v != 0 for v in row)]
    col_lines = [
        c for c in range(len(array[0])) if all(array[r][c] != 0 for r in range(len(array)))
    ]
    if len(row_lines) < 2 or len(col_lines) < 2:
        return [row[:] for row in array]
    decoded = [[0] * (len(col_lines) - 1) for _ in range(len(row_lines) - 1)]
    for row in range(len(row_lines) - 1):
        for col in range(len(col_lines) - 1):
            corners = {
                array[source_row][source_col]
                for source_row in (row_lines[row], row_lines[row + 1])
                for source_col in (col_lines[col], col_lines[col + 1])
            }
            if len(corners) == 1:
                color = next(iter(corners))
                if color != grid_color:
                    decoded[row][col] = color
    if not any(v for row in decoded for v in row):
        return [row[:] for row in array]
    return _bounding_crop(decoded, [[v != 0 for v in row] for row in decoded])


def solve(grid):
    return _decode_colored_lattice_cells([row[:] for row in grid])
