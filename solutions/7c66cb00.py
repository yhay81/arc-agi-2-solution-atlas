def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=lambda value: (counts[value], -value))
    panel_rows = []
    for row in range(height):
        frame = grid[row][0]
        interior = grid[row][1:-1]
        if (
            frame != background
            and interior
            and grid[row][-1] == frame
            and len(set(interior)) == 1
            and interior[0] != frame
        ):
            panel_rows.append((row, frame, interior[0]))
    if not panel_rows:
        return [row[:] for row in grid]
    panels = []
    start = 0
    for index in range(1, len(panel_rows) + 1):
        if index == len(panel_rows) or panel_rows[index][0] != panel_rows[index - 1][0] + 1:
            first, last = panel_rows[start], panel_rows[index - 1]
            if last[0] - first[0] >= 1 and all(
                item[1:3] == first[1:3] for item in panel_rows[start:index]
            ):
                panels.append((first[0], last[0], first[1], first[2]))
            start = index
    if not panels:
        return [row[:] for row in grid]
    panel_mask = {row for top, bottom, _, _ in panels for row in range(top, bottom + 1)}
    free = {
        (r, c)
        for r in range(height)
        for c in range(width)
        if grid[r][c] != background and r not in panel_mask
    }
    output = [row[:] for row in grid]
    for r, c in free:
        output[r][c] = background
    seen = set()
    for start_cell in sorted(free):
        if start_cell in seen:
            continue
        color = grid[start_cell[0]][start_cell[1]]
        stack = [start_cell]
        seen.add(start_cell)
        component = []
        while stack:
            r, c = stack.pop()
            component.append((r, c))
            for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (rr, cc) in free and (rr, cc) not in seen and grid[rr][cc] == color:
                    seen.add((rr, cc))
                    stack.append((rr, cc))
        bottom = max(r for r, _ in component)
        for panel_top, panel_bottom, frame, fill in panels:
            if fill != color:
                continue
            shift = panel_bottom - bottom
            for r, c in component:
                target_row = r + shift
                if panel_top <= target_row <= panel_bottom and 1 <= c < width - 1:
                    output[target_row][c] = frame
    return output
