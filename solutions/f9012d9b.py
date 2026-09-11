def solve(grid):
    height, width = len(grid), len(grid[0])
    holes = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 0]
    if not holes:
        return [row[:] for row in grid]
    for period_rows in range(1, height + 1):
        for period_cols in range(1, width + 1):
            pattern = [[None] * period_cols for _ in range(period_rows)]
            valid = True
            for row in range(height):
                for col in range(width):
                    if grid[row][col] == 0:
                        continue
                    value = grid[row][col]
                    target = (row % period_rows, col % period_cols)
                    if pattern[target[0]][target[1]] not in (None, value):
                        valid = False
                        break
                    pattern[target[0]][target[1]] = value
                if not valid:
                    break
            if not valid or any(v is None for row in pattern for v in row):
                continue
            restored = [
                [pattern[r % period_rows][c % period_cols] for c in range(width)]
                for r in range(height)
            ]
            top, left = min(r for r, _ in holes), min(c for _, c in holes)
            bottom, right = max(r for r, _ in holes), max(c for _, c in holes)
            return [row[left : right + 1] for row in restored[top : bottom + 1]]
    return [row[:] for row in grid]
