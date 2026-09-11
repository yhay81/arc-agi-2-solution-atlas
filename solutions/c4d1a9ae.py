from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = Counter(v for row in grid for v in row).most_common(1)[0][0]
    colors = sorted({v for row in grid for v in row if v != bg})
    if len(colors) < 2:
        return [r[:] for r in grid]
    boxes = []
    for color in colors:
        ps = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == color]
        boxes.append((min(c for _, c in ps), max(c for _, c in ps), color))
    boxes.sort()
    out = [r[:] for r in grid]
    for i, (left, right, _) in enumerate(boxes):
        nxt = boxes[(i + 1) % len(boxes)][2]
        for r in range(h):
            for c in range(left, right + 1):
                if grid[r][c] == bg:
                    out[r][c] = nxt
    return out
