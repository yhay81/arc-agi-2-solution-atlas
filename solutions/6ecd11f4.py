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
                        and grid[rr][cc] != 0
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        stack.append((rr, cc))
            components.append(cells)
    keys = []
    for cells in components:
        rows, cols = [r for r, _ in cells], [c for _, c in cells]
        side = max(rows) - min(rows) + 1
        if (
            side >= 2
            and max(cols) - min(cols) + 1 == side
            and len(cells) == side * side
            and len({grid[r][c] for r, c in cells}) > 1
        ):
            keys.append(cells)
    if len(keys) != 1:
        return [row[:] for row in grid]
    key = set(keys[0])
    key_rows = sorted({r for r, _ in key})
    key_cols = sorted({c for _, c in key})
    side = len(key_rows)
    if key_rows != list(range(key_rows[0], key_rows[0] + side)) or key_cols != list(
        range(key_cols[0], key_cols[0] + side)
    ):
        return [row[:] for row in grid]
    mask_cells = [cell for cells in components for cell in cells if cell not in key]
    if not mask_cells:
        return [row[:] for row in grid]
    if len({grid[r][c] for r, c in mask_cells}) != 1:
        return [row[:] for row in grid]
    top, bottom = min(r for r, _ in mask_cells), max(r for r, _ in mask_cells)
    left, right = min(c for _, c in mask_cells), max(c for _, c in mask_cells)
    mask_height, mask_width = bottom - top + 1, right - left + 1
    if mask_height % side or mask_width % side:
        return [row[:] for row in grid]
    mask = set(mask_cells)
    output = [[grid[r][c] for c in key_cols] for r in key_rows]
    for row in range(side):
        for col in range(side):
            region = {
                (r, c)
                for r in range(
                    top + row * mask_height // side, top + (row + 1) * mask_height // side
                )
                for c in range(
                    left + col * mask_width // side, left + (col + 1) * mask_width // side
                )
            }
            if not region & mask:
                output[row][col] = 0
    return output
