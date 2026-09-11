def solve(grid):
    h, w = len(grid), len(grid[0])
    unseen = {(r, c) for r in range(h) for c in range(w) if grid[r][c] == 1}
    count = 0
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
        rows = [r for r, c in cells]
        cols = [c for r, c in cells]
        if len(cells) == 4 and max(rows) - min(rows) == 1 and max(cols) - min(cols) == 1:
            count += 1
    count = min(count, 5)
    return [[1] * count + [0] * (5 - count)]
