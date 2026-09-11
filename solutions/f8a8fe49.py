def solve(grid):
    height, width = len(grid), len(grid[0])
    frame = [(row, col) for row in range(height) for col in range(width) if grid[row][col] == 2]
    top, bottom = min(row for row, _ in frame), max(row for row, _ in frame)
    left, right = min(col for _, col in frame), max(col for _, col in frame)
    center_row, center_col = (top + bottom) / 2, (left + right) / 2

    markers = {(row, col) for row in range(height) for col in range(width) if grid[row][col] == 5}
    output = [row[:] for row in grid]
    for row, col in markers:
        output[row][col] = 0

    components = []
    while markers:
        stack = [markers.pop()]
        cells = []
        while stack:
            row, col = stack.pop()
            cells.append((row, col))
            for neighbor in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if neighbor in markers:
                    markers.remove(neighbor)
                    stack.append(neighbor)
        components.append(cells)

    for cells in components:
        mean_row = sum(row for row, _ in cells) / len(cells)
        mean_col = sum(col for _, col in cells) / len(cells)
        if mean_col < left or max(col for _, col in cells) < center_col:
            side = "left"
        elif mean_col > right or min(col for _, col in cells) > center_col:
            side = "right"
        elif mean_row < top or max(row for row, _ in cells) < center_row:
            side = "top"
        elif mean_row > bottom or min(row for row, _ in cells) > center_row:
            side = "bottom"
        else:
            distances = (mean_col - left, right - mean_col, mean_row - top, bottom - mean_row)
            side = ("left", "right", "top", "bottom")[distances.index(min(distances))]

        for row, col in cells:
            if side == "left":
                target = row, 2 * left - col
            elif side == "right":
                target = row, 2 * right - col
            elif side == "top":
                target = 2 * top - row, col
            else:
                target = 2 * bottom - row, col
            if 0 <= target[0] < height and 0 <= target[1] < width:
                output[target[0]][target[1]] = 5
    return output
