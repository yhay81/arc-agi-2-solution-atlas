def _cross_lines_by_marker(array):
    vals = [v for row in array for v in row]
    background = max(set(vals), key=vals.count)
    output = [[background] * len(array[0]) for _ in array]
    rows: dict[int, list[int]] = {}
    cols: dict[int, list[int]] = {}
    for row, line in enumerate(array):
        for col, value in enumerate(line):
            if value != background:
                rows.setdefault(row, []).append(value)
                cols.setdefault(col, []).append(value)
    for row, values in rows.items():
        output[row] = [values[0]] * len(array[0])
    for col, values in cols.items():
        for row in range(len(array)):
            output[row][col] = values[0]
    for row in rows:
        for col in cols:
            if rows[row][0] != cols[col][0]:
                output[row][col] = 2
    return output


def solve(grid):
    return _cross_lines_by_marker(grid)
