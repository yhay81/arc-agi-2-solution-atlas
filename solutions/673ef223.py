def solve(grid):
    if not grid or not grid[0]:
        return [row[:] for row in grid]
    height, width = len(grid), len(grid[0])
    if width < 3:
        return [row[:] for row in grid]
    guide_color, marker_color, label_color = (2, 8, 4)
    if not any(guide_color in row for row in grid):
        return [row[:] for row in grid]
    runs = []
    for col in (0, width - 1):
        rows = [row for row in range(height) if grid[row][col] == guide_color]
        for row in rows:
            if not runs or runs[-1][2] != col or row != runs[-1][1] + 1:
                runs.append((row, row, col))
            else:
                runs[-1] = (runs[-1][0], row, col)
    if len(runs) != 2 or runs[0][2] == runs[1][2]:
        return [row[:] for row in grid]
    first, second = runs
    if first[1] - first[0] != second[1] - second[0]:
        return [row[:] for row in grid]
    marker_positions = [
        (r, c) for r in range(height) for c in range(width) if grid[r][c] == marker_color
    ]
    if not marker_positions:
        return [row[:] for row in grid]
    marker_rows = [row for row, _ in marker_positions]
    containing = [run for run in runs if all(run[0] <= row <= run[1] for row in marker_rows)]
    if len(containing) != 1:
        return [row[:] for row in grid]
    source = containing[0]
    target = second if source == first else first
    source_start, _source_stop, source_col = source
    target_start, _target_stop, target_col = target
    offset = target_start - source_start
    output = [row[:] for row in grid]
    for row, col in marker_positions:
        row, col = (int(row), int(col))
        if col in (0, width - 1):
            return [row[:] for row in grid]
        target_row = row + offset
        if not 0 <= target_row < height:
            return [row[:] for row in grid]
        output[row][col] = label_color
        if source_col == 0:
            output[row][1:col] = [marker_color] * (col - 1)
        else:
            output[row][col + 1 : width - 1] = [marker_color] * (width - col - 2)
        if target_col == 0:
            output[target_row][1:width] = [marker_color] * (width - 1)
        else:
            output[target_row][: width - 1] = [marker_color] * (width - 1)
    return output
