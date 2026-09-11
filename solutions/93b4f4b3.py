def _match(grid):
    h, w = len(grid), len(grid[0])
    if w % 2:
        return [row[:] for row in grid]
    mid = w // 2
    first = [row[:mid] for row in grid]
    second = [row[mid:] for row in grid]
    active = [r for r in range(h) if any(v != 0 for v in second[r])]
    if not active:
        return [row[:] for row in grid]
    groups = []
    for r in active:
        if not groups or r != groups[-1][-1] + 1:
            groups.append([r])
        else:
            groups[-1].append(r)
    glyphs = []
    for rows in groups:
        top, bottom = rows[0], rows[-1]
        mask = [[second[r][c] != 0 for c in range(mid)] for r in range(top, bottom + 1)]
        colors = {
            second[r][c] for r in range(top, bottom + 1) for c in range(mid) if second[r][c] != 0
        }
        if len(colors) != 1:
            return [row[:] for row in grid]
        glyphs.append((mask, next(iter(colors))))
    out = [row[:] for row in first]
    for rows in groups:
        top, bottom = rows[0], rows[-1]
        left = [[first[r][c] == 0 for c in range(mid)] for r in range(top, bottom + 1)]
        matches = [color for mask, color in glyphs if mask == left]
        if len(matches) != 1:
            return [row[:] for row in grid]
        for i, r in enumerate(range(top, bottom + 1)):
            for c in range(mid):
                if left[i][c]:
                    out[r][c] = matches[0]
    return out


def solve(grid):
    return _match(grid)
