def _yellow_components(grid):
    unseen = {
        (row, col) for row, line in enumerate(grid) for col, value in enumerate(line) if value == 4
    }
    result = []
    while unseen:
        start = unseen.pop()
        component = {start}
        queue = [start]
        for row, col in queue:
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                neighbor = row + dr, col + dc
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    component.add(neighbor)
                    queue.append(neighbor)
        result.append(component)
    return result


def solve(grid):
    height, width = len(grid), len(grid[0])
    gray = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == 5]
    handle = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == 9]
    top, bottom = min(r for r, _ in gray), max(r for r, _ in gray)
    left, right = min(c for _, c in gray), max(c for _, c in gray)
    center_row, center_col = (top + bottom) // 2, (left + right) // 2
    handle_row = sum(r for r, _ in handle) / len(handle)
    handle_col = sum(c for _, c in handle) / len(handle)
    if bottom - top > right - left:
        columns = range(center_col + 1, width) if handle_col < center_col else range(center_col)
        ray = {(center_row, col) for col in columns}
    else:
        rows = range(center_row + 1, height) if handle_row < center_row else range(center_row)
        ray = {(row, center_col) for row in rows}
    output = [row[:] for row in grid]
    for component in _yellow_components(grid):
        if component & ray:
            for row, col in component:
                output[row][col] = 7
    return output
