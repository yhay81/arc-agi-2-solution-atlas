from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    values = sorted({value for row in grid for value in row})
    counts = Counter(value for row in grid for value in row)
    if len(values) < 2:
        return [row[:] for row in grid]
    background = 5 if 5 in values else counts.most_common(1)[0][0]
    marker_values = [value for value in values if value != background]
    marker = 2 if 2 in values else min(marker_values, key=lambda value: counts[value])
    candidates = []
    for row in range(h):
        for col in range(w):
            radius = 2
            cells = (
                [(row, col)]
                + [(row + delta, col) for delta in range(-radius, radius + 1) if delta]
                + [(row, col + delta) for delta in range(-radius, radius + 1) if delta]
            )
            in_bounds = [
                (cell_row, cell_col)
                for cell_row, cell_col in cells
                if 0 <= cell_row < h and 0 <= cell_col < w
            ]
            values_here = [grid[cell_row][cell_col] for cell_row, cell_col in in_bounds]
            marker_count = sum(value == marker for value in values_here)
            if set(values_here) <= {background, marker} and marker_count >= 3:
                candidates.append((row, col, marker_count, in_bounds))
    candidates.sort(key=lambda candidate: (-candidate[2], candidate[0], candidate[1]))
    selected = []
    for candidate in candidates:
        row, col = candidate[:2]
        if any(max(abs(row - other[0]), abs(col - other[1])) <= 2 for other in selected):
            continue
        selected.append(candidate)
    output = [row[:] for row in grid]
    for row, col, _count, cells in selected:
        for cell_row, cell_col in cells:
            if output[cell_row][cell_col] == background:
                output[cell_row][cell_col] = 8
        extension = (
            [(row, col)]
            + [(row + delta, col) for delta in (-3, 3)]
            + [(row, col + delta) for delta in (-3, 3)]
        )
        in_bounds = [
            (cell_row, cell_col)
            for cell_row, cell_col in extension
            if 0 <= cell_row < h and 0 <= cell_col < w
        ]
        if any(
            (
                grid[cell_row][cell_col] == marker
                and (abs(cell_row - row) == 3 or abs(cell_col - col) == 3)
                for cell_row, cell_col in in_bounds
            )
        ) and all(
            (grid[cell_row][cell_col] in (background, marker) for cell_row, cell_col in in_bounds)
        ):
            for cell_row, cell_col in in_bounds:
                if output[cell_row][cell_col] == background:
                    output[cell_row][cell_col] = 8
    return output
