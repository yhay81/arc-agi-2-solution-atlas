def solve(grid):
    height, width = len(grid), len(grid[0])
    if width < 8:
        return [row[:] for row in grid]
    separators = [c for c in range(width) if len({grid[r][c] for r in range(height)}) == 1]
    if len(separators) < 3:
        return [row[:] for row in grid]
    left_sep, middle_sep, right_sep = separators[0], separators[1], separators[-1]
    if not left_sep < middle_sep < right_sep:
        return [row[:] for row in grid]
    reference_left, reference_right = left_sep + 1, middle_sep - 1
    target_left, target_right = middle_sep + 1, right_sep - 1
    if reference_left > reference_right or target_left > target_right:
        return [row[:] for row in grid]
    reference = [row[reference_left : reference_right + 1] for row in grid]
    counts = {}
    for row in reference:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=lambda value: (counts[value], -value))
    seen = set()
    components = []
    for row in range(height):
        for col in range(reference_right - reference_left + 1):
            if reference[row][col] == background or (row, col) in seen:
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
                        and 0 <= cc < len(reference[0])
                        and reference[rr][cc] != background
                        and (rr, cc) not in seen
                    ):
                        seen.add((rr, cc))
                        stack.append((rr, cc))
            components.append(cells)
    output = [row[:] for row in grid]
    target_inner_left, target_inner_right = target_left + 1, target_right - 1
    for cells in components:
        rows = [r for r, _ in cells]
        cols = [c for _, c in cells]
        top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)
        motif_height, motif_width = bottom - top + 1, right - left + 1
        color = reference[cells[0][0]][cells[0][1]]
        if motif_height == motif_width:
            if left == 1 and target_inner_left <= target_inner_right:
                start = target_inner_left
                end = min(target_inner_right, start + motif_height - 1)
            elif right == len(reference[0]) - 2 and target_inner_left <= target_inner_right:
                end = target_inner_right
                start = max(target_inner_left, end - motif_height + 1)
            else:
                continue
            for row in range(top, bottom + 1):
                for col in range(start, end + 1):
                    output[row][col] = color
        elif motif_width > motif_height:
            for row in range(top, bottom + 1):
                for col in range(target_inner_left, target_inner_right + 1):
                    output[row][col] = color
    return output
