def _interleave_gap_rows(array, seed_color, fill_color, background_color):
    output = [row[:] for row in array]
    if not array or not array[0]:
        return output
    if any(value not in (background_color, seed_color) for row in array for value in row):
        return output
    active_rows = [row for row in range(len(array)) if any(v == seed_color for v in array[row])]
    if len(active_rows) != 1:
        return output
    row = active_rows[0]
    previous = [c for c, v in enumerate(array[row]) if v == seed_color]
    next_color = int(fill_color)
    while len(previous) >= 2 and row + 2 < len(output):
        gaps = [a + 1 for a, b in zip(previous, previous[1:]) if b - a == 2]
        if not len(gaps):
            break
        target_row = row + 2
        for col in gaps:
            output[target_row][col] = next_color
        previous = gaps
        row = target_row
        next_color = seed_color if next_color == fill_color else fill_color
    return output


def solve(grid):
    return _interleave_gap_rows(grid, 7, 6, 3)
