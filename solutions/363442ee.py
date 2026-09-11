def solve(grid):
    height, width = len(grid), len(grid[0])
    separators = [
        c
        for c in range(width)
        if all(grid[r][c] != 0 for r in range(height))
        and len({grid[r][c] for r in range(height)}) == 1
    ]
    if len(separators) != 1:
        return [row[:] for row in grid]
    separator = separators[0]
    if separator < 1 or separator >= width - 1:
        return [row[:] for row in grid]
    left = [row[:separator] for row in grid]
    right = [row[separator + 1 :] for row in grid]
    if not any(value for row in left for value in row) or not any(
        value for row in right for value in row
    ):
        return [row[:] for row in grid]
    seen = set()
    components = []
    for row in range(height):
        for col in range(separator):
            if left[row][col] == 0 or (row, col) in seen:
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
                        and 0 <= cc < separator
                        and left[rr][cc] != 0
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        stack.append((rr, cc))
            components.append(cells)
    if not components:
        return [row[:] for row in grid]
    seed = max(components, key=len)
    if len(seed) < 2:
        return [row[:] for row in grid]
    top, bottom = min(r for r, _ in seed), max(r for r, _ in seed)
    seed_left, seed_right = min(c for _, c in seed), max(c for _, c in seed)
    pattern = [row[seed_left : seed_right + 1] for row in grid[top : bottom + 1]]
    if any(value == 0 for row in pattern for value in row):
        return [row[:] for row in grid]
    marker_values = {
        right[r][c] for r in range(height) for c in range(len(right[0])) if right[r][c] != 0
    }
    if len(marker_values) != 1:
        return [row[:] for row in grid]
    marker = next(iter(marker_values))
    output = [row[:] for row in grid]
    anchor_row, anchor_col = len(pattern) // 2, len(pattern[0]) // 2
    for marker_row in range(height):
        for relative_col in range(len(right[0])):
            if right[marker_row][relative_col] != marker:
                continue
            marker_col = relative_col + separator + 1
            for row in range(len(pattern)):
                for col in range(len(pattern[0])):
                    target_row = marker_row + row - anchor_row
                    target_col = marker_col + col - anchor_col
                    if 0 <= target_row < height and 0 <= target_col < width:
                        output[target_row][target_col] = pattern[row][col]
    return output
