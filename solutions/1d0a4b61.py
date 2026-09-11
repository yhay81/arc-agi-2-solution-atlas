def _periodic_fill(grid, missing):
    height, width = len(grid), len(grid[0])
    unknown = {
        (r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == missing
    }
    if not unknown:
        raise ValueError("No missing mask")

    candidates = []
    for row_period in range(1, height + 1):
        for col_period in range(1, width + 1):
            if row_period * col_period > height * width // 2:
                continue
            pattern = {}
            valid = True
            for row, values in enumerate(grid):
                for col, value in enumerate(values):
                    if value == missing:
                        continue
                    key = row % row_period, col % col_period
                    if key in pattern and pattern[key] != value:
                        valid = False
                        break
                    pattern[key] = value
                if not valid:
                    break
            if valid and all((r % row_period, c % col_period) in pattern for r, c in unknown):
                output = [row[:] for row in grid]
                for row, col in unknown:
                    output[row][col] = pattern[row % row_period, col % col_period]
                candidates.append((row_period * col_period, tuple(map(tuple, output))))

    if not candidates:
        raise ValueError("No supported periodic fill")
    area = min(area for area, _ in candidates)
    outputs = {output for candidate_area, output in candidates if candidate_area == area}
    if len(outputs) != 1:
        raise ValueError("Ambiguous periods")
    return [list(row) for row in outputs.pop()]


def solve(grid):
    return _periodic_fill(grid, 0)
