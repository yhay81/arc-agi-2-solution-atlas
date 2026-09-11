def solve(grid):
    h, w = len(grid), len(grid[0])
    seen = set()
    components = []
    for color in sorted({value for row in grid for value in row if value}):
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
                components.append(component)
    if not components:
        return [row[:] for row in grid]
    components.sort(
        key=lambda component: (min(c for _, c in component), min(r for r, _ in component))
    )
    output = [[0] * w for _ in range(h)]
    anchor_row = anchor_col = 0
    for component in components:
        top, bottom = min(r for r, _ in component), max(r for r, _ in component)
        left, right = min(c for _, c in component), max(c for _, c in component)
        for r, c in component:
            tr, tc = anchor_row + r - top, anchor_col + c - left
            if not (0 <= tr < h and 0 <= tc < w):
                return [row[:] for row in grid]
            output[tr][tc] = grid[r][c]
        anchor_row += bottom - top
        anchor_col += right - left
    return output
