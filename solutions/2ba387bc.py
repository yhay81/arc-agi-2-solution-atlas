def solve(grid):
    h, w = len(grid), len(grid[0])
    hollow, solid = [], []
    for color in sorted({value for row in grid for value in row if value}):
        seen = set()
        for r in range(h):
            for c in range(w):
                if grid[r][c] != color or (r, c) in seen:
                    continue
                stack = [(r, c)]
                seen.add((r, c))
                component = []
                while stack:
                    cr, cc = stack.pop()
                    component.append((cr, cc))
                    for nr, nc in ((cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)):
                        if (
                            0 <= nr < h
                            and 0 <= nc < w
                            and grid[nr][nc] == color
                            and (nr, nc) not in seen
                        ):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
                top, left = min(r for r, _ in component), min(c for _, c in component)
                bottom, right = max(r for r, _ in component), max(c for _, c in component)
                if (bottom - top + 1, right - left + 1) != (4, 4):
                    continue
                cells = {(r - top, c - left) for r, c in component}
                perimeter = {
                    (r, c) for r in range(4) for c in range(4) if r in (0, 3) or c in (0, 3)
                }
                crop = [[color if (r, c) in cells else 0 for c in range(4)] for r in range(4)]
                if cells == perimeter:
                    hollow.append((top, left, crop))
                elif len(cells) == 16:
                    solid.append((top, left, crop))
    if not hollow or not solid:
        return [row[:] for row in grid]
    hollow.sort(key=lambda item: (item[0], item[1]))
    solid.sort(key=lambda item: (item[0], item[1]))
    output = [[0] * 8 for _ in range(4 * max(len(hollow), len(solid)))]
    for index, (_, _, crop) in enumerate(hollow):
        for r in range(4):
            output[4 * index + r][:4] = crop[r]
    for index, (_, _, crop) in enumerate(solid):
        for r in range(4):
            output[4 * index + r][4:] = crop[r]
    return output
