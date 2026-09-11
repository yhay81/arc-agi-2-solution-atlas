def solve(grid):
    h, w = len(grid), len(grid[0])
    if len({value for row in grid for value in row if value}) != 1:
        return [row[:] for row in grid]
    seen = set()
    boxes = []
    for r in range(h):
        for c in range(w):
            if not grid[r][c] or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            component = []
            while stack:
                cr, cc = stack.pop()
                component.append((cr, cc))
                for nr, nc in ((cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)):
                    if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            top, bottom = min(r for r, _ in component), max(r for r, _ in component)
            left, right = min(c for _, c in component), max(c for _, c in component)
            if len(component) != (bottom - top + 1) * (right - left + 1):
                return [row[:] for row in grid]
            boxes.append((top, bottom, left, right))
    if len(boxes) < 2:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    changed = False
    for index, first in enumerate(boxes):
        for second in boxes[index + 1 :]:
            left_box, right_box = sorted((first, second), key=lambda box: box[2])
            top, bottom = max(left_box[0], right_box[0]), min(left_box[1], right_box[1])
            left, right = left_box[3] + 1, right_box[2] - 1
            if (
                top <= bottom
                and left <= right
                and all(
                    grid[r][c] == 0 for r in range(top, bottom + 1) for c in range(left, right + 1)
                )
            ):
                for r in range(top, bottom + 1):
                    output[r][left : right + 1] = [9] * (right - left + 1)
                changed = True
    return output if changed else [row[:] for row in grid]
