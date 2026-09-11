def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    template = grid[0][:]
    best = None
    for col in range(width):
        row = 0
        while row < height:
            color = grid[row][col]
            if color == background:
                row += 1
                continue
            end = row + 1
            while end < height and grid[end][col] == color:
                end += 1
            candidate = (end - row, -row, col, color)
            if candidate[0] >= 2 and (best is None or candidate > best):
                best = candidate
            row = end
    if best is None:
        return [row[:] for row in grid]
    _, neg_row, anchor_col, marker = best
    anchor_row = -neg_row
    output = [[background] * width for _ in range(height)]
    max_radius = max(anchor_col, width - 1 - anchor_col)
    for row in range(anchor_row, height):
        radius = min(row - anchor_row, max_radius)
        left, right = max(0, anchor_col - radius), min(width - 1, anchor_col + radius)
        output[row][left : right + 1] = template[left : right + 1]
        output[row][anchor_col] = marker
    return output
