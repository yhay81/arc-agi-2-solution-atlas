def solve(grid):
    height, width = len(grid), len(grid[0])
    colors = {value for row in grid for value in row if value != 0}
    if 5 not in colors or len(colors) != 2:
        return [row[:] for row in grid]
    foreground = next(color for color in colors if color != 5)
    reference = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == foreground]
    offsets = {c - r for r, c in reference}
    if len(offsets) != 1:
        return [row[:] for row in grid]
    reference_offset = next(iter(offsets))
    seen = set()
    components = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] != 5 or (row, col) in seen:
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
                        and grid[rr][cc] == 5
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        stack.append((rr, cc))
            components.append(cells)
    if not components:
        return [row[:] for row in grid]
    offsets_out = [reference_offset]
    for cells in components:
        rows = [r for r, _ in cells]
        row_values = sorted(set(rows))
        if row_values != list(range(row_values[0], row_values[-1] + 1)):
            return [row[:] for row in grid]
        counts = [rows.count(row) for row in row_values]
        side = len(counts)
        if sorted(counts) != list(range(1, side + 1)):
            return [row[:] for row in grid]
        for row in row_values:
            cols = sorted(c for r, c in cells if r == row)
            if cols != list(range(cols[0], cols[-1] + 1)):
                return [row[:] for row in grid]
        marker_offset = sum(c - r for r, c in cells) / len(cells)
        if marker_offset == reference_offset:
            return [row[:] for row in grid]
        direction = 1 if marker_offset > reference_offset else -1
        offsets_out.append(reference_offset + direction * (side + 2))
    output = [[0] * width for _ in range(height)]
    for offset in offsets_out:
        for row in range(height):
            col = row + offset
            if 0 <= col < width:
                output[row][col] = foreground
    return output
