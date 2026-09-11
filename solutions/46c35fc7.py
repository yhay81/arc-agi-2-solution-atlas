from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = counts.most_common(1)[0][0]
    remaining = {(r, c) for r in range(h) for c in range(w) if grid[r][c] != background}
    ring_order = ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0))
    source_indices = (2, 7, 4, 1, 6, 3, 0, 5)
    output = [row[:] for row in grid]
    while remaining:
        start = min(remaining)
        remaining.remove(start)
        stack = [start]
        component = [start]
        while stack:
            r, c = stack.pop()
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (nr, nc) in remaining:
                    remaining.remove((nr, nc))
                    stack.append((nr, nc))
                    component.append((nr, nc))
        if len(component) != 8:
            continue
        top, left = min(r for r, _ in component), min(c for _, c in component)
        if max(r for r, _ in component) - top != 2 or max(c for _, c in component) - left != 2:
            continue
        local = {(r - top, c - left) for r, c in component}
        if local != set(ring_order):
            continue
        source = [grid[top + r][left + c] for r, c in ring_order]
        for (r, c), index in zip(ring_order, source_indices):
            output[top + r][left + c] = source[index]
    return output
