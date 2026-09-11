from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = counts.most_common(1)[0][0]

    def components(cells):
        remaining = set(cells)
        found = []
        while remaining:
            seed = min(remaining)
            remaining.remove(seed)
            stack = [seed]
            component = [seed]
            while stack:
                r, c = stack.pop()
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        point = (r + dr, c + dc)
                        if (dr or dc) and point in remaining:
                            remaining.remove(point)
                            stack.append(point)
                            component.append(point)
            found.append(component)
        return found

    regions = components((r, c) for r in range(h) for c in range(w) if grid[r][c] != background)
    if not regions:
        return [row[:] for row in grid]
    panel = max(regions, key=len)
    top, bottom = min(r for r, _ in panel), max(r for r, _ in panel)
    left, right = min(c for _, c in panel), max(c for _, c in panel)
    if len(panel) != (bottom - top + 1) * (right - left + 1):
        return [row[:] for row in grid]
    output = [row[left : right + 1] for row in grid[top : bottom + 1]]
    key_colors = sorted({grid[r][c] for r, c in panel if grid[r][c] not in (0, background)})
    outside = {
        (r, c)
        for r in range(h)
        for c in range(w)
        if not (top <= r <= bottom and left <= c <= right)
    }
    for color in key_colors:
        key_positions = [(r - top, c - left) for r, c in panel if grid[r][c] == color]
        if len(key_positions) != 1:
            return [row[:] for row in grid]
        object_count = len(components((r, c) for r, c in outside if grid[r][c] == color))
        row, first_col = key_positions[0]
        output[row] = [0] * len(output[0])
        for index in range(object_count):
            col = first_col + 2 * index
            if col >= len(output[0]):
                return [row[:] for row in grid]
            output[row][col] = color
    return output
