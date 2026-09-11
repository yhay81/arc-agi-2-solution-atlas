def solve(grid):
    remaining = {(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 0}
    out = [row[:] for row in grid]
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        component, stack = {start}, [start]
        while stack:
            r, c = stack.pop()
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in remaining:
                    remaining.remove(point)
                    component.add(point)
                    stack.append(point)
        if len(component) >= 2:
            for r, c in component:
                out[r][c] = 8
    return out
