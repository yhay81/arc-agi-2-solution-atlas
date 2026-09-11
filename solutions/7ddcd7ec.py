def solve(grid):
    height, width = len(grid), len(grid[0])
    colors = {cell for row in grid for cell in row if cell}
    if len(colors) != 1:
        return [row[:] for row in grid]
    color = colors.pop()
    positions = [
        (r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == color
    ]
    blocks = [
        (r, c)
        for r in range(height - 1)
        for c in range(width - 1)
        if all(grid[r + dr][c + dc] == color for dr in (0, 1) for dc in (0, 1))
    ]
    if len(blocks) != 1:
        return [row[:] for row in grid]
    top, left = blocks[0]
    block_cells = {(top + dr, left + dc) for dr in (0, 1) for dc in (0, 1)}
    markers = [(r, c) for r, c in positions if (r, c) not in block_cells]
    if not markers:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for row, col in markers:
        dr, dc = row * 2 - 2 * top - 1, col * 2 - 2 * left - 1
        if abs(dr) != abs(dc):
            return [row[:] for row in grid]
        dr, dc = (dr > 0) - (dr < 0), (dc > 0) - (dc < 0)
        row, col = row + dr, col + dc
        while 0 <= row < height and 0 <= col < width:
            output[row][col] = color
            row, col = row + dr, col + dc
    return output
