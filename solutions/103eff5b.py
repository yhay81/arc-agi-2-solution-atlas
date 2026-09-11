def solve(grid):
    height, width = len(grid), len(grid[0])
    marker = 8
    marker_mask = [[value == marker for value in row] for row in grid]
    marker_rows = [r for r, row in enumerate(marker_mask) if any(row)]
    key_cells = [
        (r, c)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value not in (0, marker)
    ]
    if not marker_rows or not key_cells:
        return [row[:] for row in grid]
    top, bottom = min(r for r, _ in key_cells), max(r for r, _ in key_cells)
    left, right = min(c for _, c in key_cells), max(c for _, c in key_cells)
    groups = []
    for row in range(marker_rows[0], height):
        if not any(marker_mask[row]):
            continue
        if not groups or marker_mask[row] != marker_mask[groups[-1][1]]:
            groups.append([row, row])
        else:
            groups[-1][1] = row
    if len(groups) != right - left + 1:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for key_col, (start, end) in enumerate(groups):
        repeat = end - start + 1
        positions = [c for c, present in enumerate(marker_mask[start]) if present]
        runs = []
        for col in positions:
            if not runs or col > runs[-1][-1] + 1:
                runs.append([col])
            else:
                runs[-1].append(col)
        slots = []
        for run in runs:
            if len(run) % repeat:
                return [row[:] for row in grid]
            slots.extend(run[i : i + repeat] for i in range(0, len(run), repeat))
        colors = [
            grid[row][left + key_col] for row in range(top, bottom + 1) if grid[row][left + key_col]
        ][::-1]
        if len(slots) != len(colors):
            return [row[:] for row in grid]
        for slot, color in zip(slots, colors):
            for row in range(start, end + 1):
                for col in slot:
                    output[row][col] = color
    return output
