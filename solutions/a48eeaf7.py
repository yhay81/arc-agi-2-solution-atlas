def solve(grid):
    height, width = len(grid), len(grid[0])
    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 0 or (row, col) in seen:
                continue
            stack = [(row, col)]
            seen.add((row, col))
            cells = []
            while stack:
                r, c = stack.pop()
                cells.append((r, c))
                for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (
                        0 <= rr < height
                        and 0 <= cc < width
                        and grid[rr][cc]
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        stack.append((rr, cc))
            components.append(cells)
    if len(components) < 2:
        return [row[:] for row in grid]
    largest_size = max(map(len, components))
    largest = [cells for cells in components if len(cells) == largest_size]
    if len(largest) != 1 or largest_size < 4:
        return [row[:] for row in grid]
    body = largest[0]
    markers = [cells for cells in components if cells is not body]
    if any(len(cells) != 1 for cells in markers):
        return [row[:] for row in grid]
    rows = [r for r, _ in body]
    cols = [c for _, c in body]
    top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)
    if len(body) != (bottom - top + 1) * (right - left + 1):
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    marker_values = []
    for cells in markers:
        row, col = cells[0]
        marker_values.append((row, col, grid[row][col]))
        output[row][col] = 0
    min_row, max_row = max(0, top - 1), min(height - 1, bottom + 1)
    min_col, max_col = max(0, left - 1), min(width - 1, right + 1)
    for row, col, color in marker_values:
        output[min(max(row, min_row), max_row)][min(max(col, min_col), max_col)] = color
    return output
