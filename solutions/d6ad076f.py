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
    if len(components) != 2:
        return [row[:] for row in grid]
    boxes, colors = [], []
    for cells in components:
        top, bottom = min(r for r, _ in cells), max(r for r, _ in cells)
        left, right = min(c for _, c in cells), max(c for _, c in cells)
        color = grid[cells[0][0]][cells[0][1]]
        if len(cells) != (bottom - top + 1) * (right - left + 1) or any(
            grid[r][c] != color for r in range(top, bottom + 1) for c in range(left, right + 1)
        ):
            return [row[:] for row in grid]
        boxes.append((top, bottom, left, right))
        colors.append(color)
    if colors[0] == colors[1]:
        return [row[:] for row in grid]
    candidates = []
    left_box, right_box = sorted(boxes, key=lambda box: box[2])
    overlap_top, overlap_bottom = max(left_box[0], right_box[0]), min(left_box[1], right_box[1])
    gap_left, gap_right = left_box[3] + 1, right_box[2] - 1
    if gap_left <= gap_right and overlap_top + 1 <= overlap_bottom - 1:
        candidates.append((overlap_top + 1, overlap_bottom - 1, gap_left, gap_right))
    top_box, bottom_box = sorted(boxes, key=lambda box: box[0])
    overlap_left, overlap_right = max(top_box[2], bottom_box[2]), min(top_box[3], bottom_box[3])
    gap_top, gap_bottom = top_box[1] + 1, bottom_box[0] - 1
    if gap_top <= gap_bottom and overlap_left + 1 <= overlap_right - 1:
        candidates.append((gap_top, gap_bottom, overlap_left + 1, overlap_right - 1))
    if len(candidates) != 1:
        return [row[:] for row in grid]
    top, bottom, left, right = candidates[0]
    if any(grid[r][c] != 0 for r in range(top, bottom + 1) for c in range(left, right + 1)):
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for r in range(top, bottom + 1):
        for c in range(left, right + 1):
            output[r][c] = 8
    return output
