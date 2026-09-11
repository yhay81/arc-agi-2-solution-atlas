def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [r[:] for r in grid]
    occupied = {(r, c) for r in range(h) for c in range(w) if grid[r][c]}
    while occupied:
        seed = occupied.pop()
        comp = {seed}
        stack = [seed]
        while stack:
            r, c = stack.pop()
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    p = (r + dr, c + dc)
                    if p in occupied:
                        occupied.remove(p)
                        comp.add(p)
                        stack.append(p)
        top, bottom = min(r for r, _ in comp), max(r for r, _ in comp)
        left, right = min(c for _, c in comp), max(c for _, c in comp)
        for r in range(top, bottom + 1):
            for c in range(left, right + 1):
                if out[r][c] == 0:
                    out[r][c] = 1
    return [[7 if v == 1 else v for v in row] for row in out]
