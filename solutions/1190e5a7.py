def _separator_lattice_background(array):
    values = [v for row in array for v in row]
    if not values:
        return [row[:] for row in array]
    background = max(set(values), key=values.count)
    rows = [
        row
        for row in range(len(array))
        if all(v != background for v in array[row]) and len(set(array[row])) == 1
    ]
    cols = [
        col
        for col in range(len(array[0]))
        if all(row[col] != background for row in array) and len({row[col] for row in array}) == 1
    ]
    if not rows and (not cols):
        return [row[:] for row in array]
    return [[background] * (len(cols) + 1) for _ in range(len(rows) + 1)]


def solve(grid):
    return _separator_lattice_background(grid)
