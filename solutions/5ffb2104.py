def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [[0] * w for _ in range(h)]
    comps = []
    for color in sorted({v for row in grid for v in row if v}):
        unseen = {(r, c) for r in range(h) for c in range(w) if grid[r][c] == color}
        while unseen:
            stack = [unseen.pop()]
            cells = []
            while stack:
                r, c = stack.pop()
                cells.append((r, c))
                for q in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if q in unseen:
                        unseen.remove(q)
                        stack.append(q)
            comps.append((max(c for r, c in cells), cells, color))
    comps.sort(reverse=True, key=lambda x: x[0])
    for _, cells, color in comps:
        shift = 0
        while all(c + shift + 1 < w and out[r][c + shift + 1] == 0 for r, c in cells):
            shift += 1
        for r, c in cells:
            out[r][c + shift] = color
    return out
