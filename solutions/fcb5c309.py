def solve(grid):
    height, width = len(grid), len(grid[0])
    best = None
    colors = {value for row in grid for value in row if value != 0}
    for frame_color in colors:
        seen = set()
        for row in range(height):
            for col in range(width):
                if grid[row][col] != frame_color or (row, col) in seen:
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
                            and grid[rr][cc] == frame_color
                            and (rr, cc) not in seen
                        ):
                            seen.add((rr, cc))
                            stack.append((rr, cc))
                top, left = min(r for r, _ in cells), min(c for _, c in cells)
                bottom, right = max(r for r, _ in cells), max(c for _, c in cells)
                if bottom <= top or right <= left:
                    continue
                perimeter = (
                    {(top, c) for c in range(left, right + 1)}
                    | {(bottom, c) for c in range(left, right + 1)}
                    | {(r, left) for r in range(top, bottom + 1)}
                    | {(r, right) for r in range(top, bottom + 1)}
                )
                candidate = (
                    (bottom - top + 1) * (right - left + 1),
                    top,
                    left,
                    bottom,
                    right,
                    frame_color,
                )
                if set(cells) == perimeter and (best is None or candidate[0] > best[0]):
                    best = candidate
    if best is None:
        return [row[:] for row in grid]
    _, top, left, bottom, right, frame_color = best
    accents = colors - {frame_color}
    if len(accents) != 1:
        return [row[:] for row in grid]
    accent = next(iter(accents))
    output = [row[left : right + 1] for row in grid[top : bottom + 1]]
    for row in output:
        for col in range(len(row)):
            if row[col] == frame_color:
                row[col] = accent
    return output
