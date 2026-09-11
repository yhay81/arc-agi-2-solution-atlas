from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = counts.most_common(1)[0][0]
    rectangles = []
    for color in sorted(counts):
        if color == background:
            continue
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
                rows = [row for row, _ in component]
                cols = [col for _, col in component]
                top, bottom = (min(rows), max(rows))
                left, right = (min(cols), max(cols))
                box_h, box_w = (bottom - top + 1, right - left + 1)
                if len(component) == box_h * box_w and top >= box_h:
                    rectangles.append((color, top, bottom, left, right))
    if not rectangles:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for _color, top, bottom, left, right in rectangles:
        for r in range(top, bottom + 1):
            output[r][left : right + 1] = [background] * (right - left + 1)
    for color, top, bottom, left, right in rectangles:
        height = bottom - top + 1
        for r in range(top - height, bottom - height + 1):
            output[r][left : right + 1] = [color] * (right - left + 1)
    return output
