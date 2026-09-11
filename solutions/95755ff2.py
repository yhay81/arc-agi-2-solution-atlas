def solve(grid):
    height, width = len(grid), len(grid[0])
    positions = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == 2]
    if not positions:
        return [row[:] for row in grid]
    center = radius = None
    for center_row in range(height):
        for center_col in range(width):
            distances = [abs(r - center_row) + abs(c - center_col) for r, c in positions]
            if len(set(distances)) != 1 or distances[0] <= 0:
                continue
            candidate_radius = distances[0]
            boundary = {
                (r, c)
                for r in range(height)
                for c in range(width)
                if abs(r - center_row) + abs(c - center_col) == candidate_radius
            }
            if len(boundary) == len(positions) and boundary == set(positions):
                center, radius = (center_row, center_col), candidate_radius
                break
        if center is not None:
            break
    if center is None:
        return [row[:] for row in grid]
    center_row, center_col = center
    interior = {
        (r, c)
        for r in range(height)
        for c in range(width)
        if abs(r - center_row) + abs(c - center_col) < radius
    }
    output = [row[:] for row in grid]
    for row in range(height):
        cols = [col for col in range(width) if (row, col) in interior]
        if not cols:
            continue
        left, right = cols[0], cols[-1]
        left_markers = [col for col in range(left) if grid[row][col] not in (0, 2)]
        right_markers = [col for col in range(right + 1, width) if grid[row][col] not in (0, 2)]
        for source_col, cells in (
            (left_markers[-1] if left_markers else None, range(left, right + 1)),
            (right_markers[0] if right_markers else None, range(right, left - 1, -1)),
        ):
            if source_col is None:
                continue
            color = grid[row][source_col]
            for col in cells:
                if (row, col) not in interior:
                    continue
                if grid[row][col] not in (0, 2):
                    break
                if output[row][col] == 0:
                    output[row][col] = color
    for col in range(width):
        rows = [row for row in range(height) if (row, col) in interior]
        if not rows:
            continue
        top, bottom = rows[0], rows[-1]
        top_markers = [row for row in range(top) if grid[row][col] not in (0, 2)]
        bottom_markers = [row for row in range(bottom + 1, height) if grid[row][col] not in (0, 2)]
        for source_row, cells in (
            (top_markers[-1] if top_markers else None, range(top, bottom + 1)),
            (bottom_markers[0] if bottom_markers else None, range(bottom, top - 1, -1)),
        ):
            if source_row is None:
                continue
            color = grid[source_row][col]
            for row in cells:
                if (row, col) not in interior:
                    continue
                if grid[row][col] not in (0, 2):
                    break
                if output[row][col] == 0:
                    output[row][col] = color
    return output
