def solve(grid):
    occurrences = {}
    height, width = len(grid), len(grid[0])
    for top in range(height - 2):
        for left in range(width - 2):
            glyph = [row[left : left + 3] for row in grid[top : top + 3]]
            values = {value for row in glyph for value in row if value != 0}
            if len(values) != 1:
                continue
            if (
                not any(v for v in glyph[0])
                or not any(row[0] for row in glyph)
                or not any(v for v in glyph[2])
                or not any(row[2] for row in glyph)
            ):
                continue
            color = next(iter(values))
            key = (color, tuple(value for row in glyph for value in row))
            occurrences.setdefault(key, []).append((top, left))
    if not occurrences:
        return [row[:] for row in grid]
    max_count = max(len(locations) for locations in occurrences.values())
    candidates = [key for key, locations in occurrences.items() if len(locations) == max_count]
    if len(candidates) != 1 or max_count < 2:
        return [row[:] for row in grid]
    color, values = candidates[0]
    del color
    return [list(values[i : i + 3]) for i in range(0, 9, 3)]
