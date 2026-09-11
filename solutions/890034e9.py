from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    templates = []
    counts = Counter(value for row in grid for value in row)
    for marker in sorted(counts):
        if marker == 0 or counts[marker] < 8:
            continue
        points = {(r, c) for r in range(h) for c in range(w) if grid[r][c] == marker}
        top, bottom = min(r for r, _ in points), max(r for r, _ in points)
        left, right = min(c for _, c in points), max(c for _, c in points)
        height, width = bottom - top + 1, right - left + 1
        if height < 3 or width < 3:
            continue
        perimeter = {
            (r, c)
            for r in range(top, bottom + 1)
            for c in range(left, right + 1)
            if r in (top, bottom) or c in (left, right)
        }
        if points == perimeter and all(
            grid[r][c] == 0 for r in range(top + 1, bottom) for c in range(left + 1, right)
        ):
            templates.append((marker, height, width, top, left))
    if len(templates) != 1:
        return [row[:] for row in grid]
    marker, height, width, template_top, template_left = templates[0]
    candidates = []
    for top in range(h - height + 1):
        for left in range(w - width + 1):
            if (top, left) == (template_top, template_left):
                continue
            if any(
                grid[r][c] != 0
                for r in range(top + 1, top + height - 1)
                for c in range(left + 1, left + width - 1)
            ):
                continue
            border = [
                grid[r][c]
                for r in range(top, top + height)
                for c in range(left, left + width)
                if r in (top, top + height - 1) or c in (left, left + width - 1)
            ]
            nonzero = sum(value != 0 for value in border)
            if nonzero:
                candidates.append((nonzero, top, left))
    if not candidates:
        return [row[:] for row in grid]
    _, top, left = max(candidates)
    output = [row[:] for row in grid]
    for c in range(left, left + width):
        output[top][c] = output[top + height - 1][c] = marker
    for r in range(top, top + height):
        output[r][left] = output[r][left + width - 1] = marker
    return output
