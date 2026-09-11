def _dedupe_rows_cols(array):
    rows = [array[0][:]]
    rows.extend(row[:] for row in array[1:] if row != rows[-1])
    compact = rows
    keep_cols = [0]
    keep_cols.extend(
        col
        for col in range(1, len(compact[0]))
        if [row[col] for row in compact] != [row[keep_cols[-1]] for row in compact]
    )
    return [[row[c] for c in keep_cols] for row in compact]


def solve(grid):
    return _dedupe_rows_cols(grid)
