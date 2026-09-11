def solve(grid):
    a = grid
    a = [row[:] for row in a]
    nonempty_rows = [row for row in a if any(value != 7 for value in row)]
    if not nonempty_rows:
        raise ValueError("Expected at least one two-color pair")
    first = [value for value in nonempty_rows[0] if value != 7]
    if len(first) != 2 or first[0] == first[1]:
        raise ValueError("Expected a two-color reference pair")
    out = [[7] * len(a[0]) for _ in a]
    for r, row in enumerate(a):
        columns = [c for c, value in enumerate(row) if value != 7]
        if not len(columns):
            continue
        if len(columns) != 2 or columns[1] != columns[0] + 1:
            raise ValueError("Expected one adjacent pair per row")
        values = [row[c] for c in columns]
        if values not in (first, first[::-1]):
            raise ValueError("Unexpected pair colors")
        shift = int(values == first[::-1])
        if columns[-1] + shift >= len(a[0]):
            raise ValueError("Shift leaves the grid")
        out[r][columns[0] + shift : columns[0] + shift + 2] = values
    return out
