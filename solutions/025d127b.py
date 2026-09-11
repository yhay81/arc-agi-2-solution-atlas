def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [[0] * w for _ in range(h)]
    unseen = {(r, c) for r in range(h) for c in range(w) if grid[r][c]}
    while unseen:
        seed = unseen.pop()
        stack = [seed]
        cells = [seed]
        while stack:
            r, c = stack.pop()
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    p = (r + dr, c + dc)
                    if (dr or dc) and p in unseen:
                        unseen.remove(p)
                        stack.append(p)
                        cells.append(p)
        bottom = max(r for r, _ in cells)
        rows = {r for r, _ in cells}
        right = {r: max(c for rr, c in cells if rr == r) for r in rows}
        for r, c in cells:
            fixed = r == bottom or (r == bottom - 1 and c == right[r])
            out[r][c if fixed else min(c + 1, w - 1)] = grid[r][c]
    return out
