def solve(grid):
    a = grid
    out = [row[:] for row in a]
    row_order = [(r, c) for r, row in enumerate(a) for c, v in enumerate(row) if v != 7]
    col_order = sorted(row_order, key=lambda point: (point[1], point[0]))
    one_per_row = len({r for r, c in row_order}) == len(row_order)
    one_per_col = len({c for r, c in row_order}) == len(row_order)
    if one_per_row and one_per_col and (row_order != col_order):
        raise ValueError("Both reading axes are possible and disagree")
    if not one_per_row and (not one_per_col):
        raise ValueError("No axis has at most one point per line")
    order = row_order if one_per_row else col_order
    for index, (r, c) in enumerate(order):
        out[r][c] = (2, 8, 5)[index % 3]
    return out
