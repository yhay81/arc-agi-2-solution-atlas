from collections import Counter


def _runs(blocked: set[int], limit: int) -> list[tuple[int, int]]:
    result = []
    start = None
    for i in range(limit + 1):
        if i < limit and i not in blocked:
            start = i if start is None else start
        elif start is not None:
            result.append((start, i))
            start = None
    return result


def solve(grid):
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    counts = Counter(value for row in grid for value in row if value != background)
    separator = counts.most_common(1)[0][0]
    sep_cells = [
        (r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == separator
    ]
    top, bottom = min(r for r, _ in sep_cells), max(r for r, _ in sep_cells)
    left, right = min(c for _, c in sep_cells), max(c for _, c in sep_cells)
    row_lines = {
        r
        for r in range(top, bottom + 1)
        if all(grid[r][c] == separator for c in range(left, right + 1))
    }
    col_lines = {
        c
        for c in range(left, right + 1)
        if all(grid[r][c] == separator for r in range(top, bottom + 1))
    }
    row_runs = _runs(row_lines, len(grid))
    col_runs = _runs(col_lines, len(grid[0]))
    row_runs = [(a, b) for a, b in row_runs if a > top and b - 1 < bottom]
    col_runs = [(a, b) for a, b in col_runs if a > left and b - 1 < right]
    output = []
    for a, b in row_runs:
        row = []
        for c, d in col_runs:
            colors = [
                grid[r][x]
                for r in range(a, b)
                for x in range(c, d)
                if grid[r][x] not in (background, separator)
            ]
            row.append(Counter(colors).most_common(1)[0][0] if colors else background)
        output.append(row)
    return output
