def solve(grid):
    height, width = len(grid), len(grid[0])
    rows = [r for r, row in enumerate(grid) if len(set(row)) == 1 and row[0]]
    cols = [c for c in range(width) if len({grid[r][c] for r in range(height)}) == 1 and grid[0][c]]
    if not rows or not cols:
        return [row[:] for row in grid]
    row_edges = [-1, *rows, height]
    col_edges = [-1, *cols, width]
    top, bottom = row_edges[0] + 2, row_edges[1] - 1
    left, right = col_edges[0] + 2, col_edges[1] - 1
    if top >= bottom or left >= right:
        return [row[:] for row in grid]
    template = [[grid[r][c] != 0 for c in range(left, right)] for r in range(top, bottom)]
    if not any(any(row) for row in template):
        return [row[:] for row in grid]
    frame = grid[rows[0]][0]
    output = [row[:] for row in grid]
    for i in range(len(row_edges) - 1):
        top, bottom = row_edges[i] + 2, row_edges[i + 1] - 1
        for j in range(len(col_edges) - 1):
            left, right = col_edges[j] + 2, col_edges[j + 1] - 1
            if bottom - top != len(template) or right - left != len(template[0]):
                continue
            for r in range(top, bottom):
                for c in range(left, right):
                    if template[r - top][c - left] and grid[r][c] == 0:
                        output[r][c] = frame
    return output
