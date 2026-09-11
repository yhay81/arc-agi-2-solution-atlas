def solve(grid):
    source = [row[:] for row in grid]
    h, w = len(source), len(source[0])
    seed = [(r, c) for r in range(h) for c in range(w) if source[r][c] == 8]
    if not seed:
        return source
    top, left = min(r for r, _ in seed), min(c for _, c in seed)
    template = [(r - top, c - left) for r, c in seed]
    th = max(r for r, _ in template) + 1
    tw = max(c for _, c in template) + 1

    def paint(canvas):
        out = [row[:] for row in canvas]
        for r in range(len(canvas)):
            for c in range(len(canvas[0])):
                cells = [(r + dr, c + dc) for dr, dc in template]
                if max(x for x, _ in cells) >= len(canvas) or max(y for _, y in cells) >= len(
                    canvas[0]
                ):
                    continue
                if all(canvas[x][y] == 3 for x, y in cells):
                    for x, y in cells:
                        out[x][y] = 8
        return out

    def rotate(a):
        return [list(row) for row in zip(*a[::-1])]

    out = source
    for _ in range(4):
        out = rotate(paint(out))
    trans = [list(row) for row in zip(*out)]
    trans = paint(trans)
    return [list(row) for row in zip(*trans)]
