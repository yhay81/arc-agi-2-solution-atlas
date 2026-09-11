def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 8 or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                r, c = stack.pop()
                cells.append((r, c))
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        rr, cc = r + dr, c + dc
                        if (
                            0 <= rr < height
                            and 0 <= cc < width
                            and grid[rr][cc] == 8
                            and (rr, cc) not in seen
                        ):
                            seen.add((rr, cc))
                            stack.append((rr, cc))
            components.append(cells)
    for component in components:
        rows = [r for r, _ in component]
        cols = [c for _, c in component]
        max_col = max(cols)
        if max_col == width - 1:
            continue
        if min(rows) == max(rows):
            row = rows[0]
            for col in range(max_col + 1, width):
                output[row][col] = 1
            continue
        row_columns = {
            row: sorted(c for r, c in component if r == row) for row in sorted(set(rows))
        }
        row_runs = [
            any(right == left + 1 for left, right in zip(columns, columns[1:]))
            for columns in row_columns.values()
        ]
        if any(row_runs) and any(len(columns) == 1 for columns in row_columns.values()):
            target_row = max(rows) + 1
            if target_row < height:
                for col in range(max_col + 1, width):
                    output[target_row][col] = 1
        elif any(row_runs) and all(len(columns) > 1 for columns in row_columns.values()):
            for row, columns in row_columns.items():
                if max(columns) == max_col:
                    for col in range(max_col + 1, width):
                        output[row][col] = 1
        else:
            differences = [
                right - left
                for columns in row_columns.values()
                for left, right in zip(columns, columns[1:])
                if right > left
            ]
            if not differences:
                unique_cols = sorted(set(cols))
                differences = [
                    right - left
                    for left, right in zip(unique_cols, unique_cols[1:])
                    if right > left
                ]
            period = min(differences, default=1)
            for row, columns in row_columns.items():
                phase = min(columns) % period
                for col in range(max(columns) + 1, width):
                    if col % period == phase:
                        output[row][col] = 1
    return output
