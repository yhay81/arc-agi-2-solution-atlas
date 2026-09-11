from collections import Counter


def _runs(indices: list[int], limit: int) -> list[tuple[int, int]]:
    blocked = set(indices)
    runs = []
    start = None
    for index in range(limit + 1):
        if index < limit and index not in blocked:
            start = index if start is None else start
        elif start is not None:
            runs.append((start, index))
            start = None
    return runs


def solve(grid):
    counts = Counter(value for row in grid for value in row if value)
    separator = counts.most_common(1)[0][0]
    rows = [r for r, row in enumerate(grid) if all(value == separator for value in row)]
    columns = [c for c in range(len(grid[0])) if all(row[c] == separator for row in grid)]
    row_runs = _runs(rows, len(grid))
    column_runs = _runs(columns, len(grid[0]))
    seeds = []
    for ir, (top, bottom) in enumerate(row_runs):
        for ic, (left, right) in enumerate(column_runs):
            patch = [row[left:right] for row in grid[top:bottom]]
            if any(value not in (0, separator) for row in patch for value in row):
                seeds.append((ir, ic, patch))
    seed_row, seed_column, patch = seeds[0]
    output = [row[:] for row in grid]
    for ir, (top, bottom) in enumerate(row_runs):
        for ic, (left, right) in enumerate(column_runs):
            if (ir - seed_row) % 2 == 0 and (ic - seed_column) % 2 == 0:
                for dr, row in enumerate(patch[: bottom - top]):
                    output[top + dr][left:right] = row[: right - left]
    return output
