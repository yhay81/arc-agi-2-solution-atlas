def solve(grid):
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    for start_row in range(height):
        for start_col in range(width):
            if not grid[start_row][start_col] or (start_row, start_col) in seen:
                continue
            color = grid[start_row][start_col]
            queue, points = [(start_row, start_col)], []
            seen.add((start_row, start_col))
            while queue:
                row, col = queue.pop()
                points.append((row, col))
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    point = row + dr, col + dc
                    if (
                        0 <= point[0] < height
                        and 0 <= point[1] < width
                        and point not in seen
                        and grid[point[0]][point[1]] == color
                    ):
                        seen.add(point)
                        queue.append(point)
            if len(points) < 4:
                continue
            top, bottom = min(r for r, _ in points), max(r for r, _ in points)
            left, right = min(c for _, c in points), max(c for _, c in points)
            missing = [
                (r, c)
                for r in range(top, bottom + 1)
                for c in range(left, right + 1)
                if grid[r][c] != color
            ]
            if not missing or any(grid[r][c] for r, c in missing):
                continue
            marker_rows = {r - top for r, _ in missing}
            marker_cols = {c - left for _, c in missing}
            if right - left + 1 > bottom - top + 1:
                for col in marker_cols:
                    for row in range(top, bottom + 1):
                        output[row][left + col] = 0
            elif bottom - top + 1 > right - left + 1:
                for row in marker_rows:
                    output[top + row][left : right + 1] = [0] * (right - left + 1)
    return output
