def solve(grid):
    height, width = len(grid), len(grid[0])
    marker_rows = [
        r
        for r, row in enumerate(grid)
        if row.count(2) >= 2 and row.count(2) == sum(bool(x) for x in row)
    ]
    marker_cols = [
        c
        for c in range(width)
        if sum(grid[r][c] == 2 for r in range(height)) >= 2
        and sum(bool(grid[r][c]) for r in range(height))
        == sum(grid[r][c] == 2 for r in range(height))
    ]
    output = [row[:] for row in grid]
    for top, bottom in zip([-1] + marker_rows, marker_rows + [height]):
        for left, right in zip([-1] + marker_cols, marker_cols + [width]):
            cells = [
                (r, c)
                for r in range(top + 1, bottom)
                for c in range(left + 1, right)
                if grid[r][c] == 1
            ]
            if not cells:
                continue
            for r, c in cells:
                output[r][c] = 0
            first_row = min(r for r, _ in cells)
            last_row = max(r for r, _ in cells)
            low_row = top + 1 + (bottom - top - 1 - (last_row - first_row + 1)) // 2
            high_row = low_row + (bottom - top - 1 - (last_row - first_row + 1)) % 2
            target_row = min((low_row, high_row), key=lambda r: abs(first_row - r))
            for source_row in range(first_row, last_row + 1):
                cols = [c for r, c in cells if r == source_row]
                if not cols:
                    continue
                object_width = cols[-1] - cols[0] + 1
                low_col = left + 1 + (right - left - 1 - object_width) // 2
                high_col = low_col + (right - left - 1 - object_width) % 2
                target_col = min((low_col, high_col), key=lambda c: abs(cols[0] - c))
                for col in cols:
                    output[target_row + source_row - first_row][target_col + col - cols[0]] = 1
    return output
