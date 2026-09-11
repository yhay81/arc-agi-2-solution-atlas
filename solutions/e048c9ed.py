from collections import Counter


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    out = [row[:] for row in a]
    marker_row, marker_col = next(
        (r, c) for r, row in enumerate(a) for c, value in enumerate(row) if value == 5
    )
    bars = []
    for row in range(len(a)):
        length = sum(
            a[row][col] != 0 and (row, col) != (marker_row, marker_col) for col in range(len(a[0]))
        )
        if length:
            bars.append((row, length))
    ordinary = [length for row, length in bars if 5 not in a[row]]
    repeated = next((length for length, count in Counter(ordinary).items() if count > 1), None)
    for row, length in bars:
        base = length - repeated if repeated is not None and length != repeated else length - 1
        out[row][marker_col] = base * base % 10
    return out
