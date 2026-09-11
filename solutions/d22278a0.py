def solve(grid):
    height, width = len(grid), len(grid[0])
    corners = {(0, 0), (0, width - 1), (height - 1, 0), (height - 1, width - 1)}
    markers = [(r, c, grid[r][c]) for r, c in corners if grid[r][c]]
    if len(markers) < 2 or any(
        grid[r][c] and (r, c) not in corners for r in range(height) for c in range(width)
    ):
        return [row[:] for row in grid]
    output = [[0] * width for _ in range(height)]
    for row in range(height):
        for col in range(width):
            distances = [abs(row - r) + abs(col - c) for r, c, _ in markers]
            nearest = min(distances)
            indices = [i for i, distance in enumerate(distances) if distance == nearest]
            if len(indices) != 1:
                continue
            top, left, color = markers[indices[0]]
            row_distance, col_distance = abs(row - top), abs(col - left)
            if (
                (row_distance % 2 == 0 and col_distance % 2 == 0)
                or (row_distance % 2 == 0 and col_distance % 2 and row_distance > col_distance)
                or (row_distance % 2 and col_distance % 2 == 0 and col_distance > row_distance)
            ):
                output[row][col] = color
    return output
