from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    nonzero = [value for row in grid for value in row if value]
    if len(set(nonzero)) < 3:
        return [row[:] for row in grid]
    counts = Counter(nonzero)
    payload = counts.most_common(1)[0][0]
    seen = set()
    components = []
    for r in range(h):
        for c in range(w):
            if grid[r][c] != payload or (r, c) in seen:
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
                        and grid[nr][nc] == payload
                        and (nr, nc) not in seen
                    ):
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            components.append(component)
    if len(components) < 2:
        return [row[:] for row in grid]
    first_row = min(r for component in components for r, _ in component)
    header_rows = [r for r in range(first_row) if any(grid[r][c] != 0 for c in range(w))]
    if len(header_rows) != 1:
        return [row[:] for row in grid]
    header = header_rows[0]
    markers = [(c, grid[header][c]) for c in range(w) if grid[header][c]]
    if len(markers) != len(components) or any(color == payload for _, color in markers):
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for component in components:
        left, right = min(c for _, c in component), max(c for _, c in component)
        if len(component) != (max(r for r, _ in component) - min(r for r, _ in component) + 1) * (
            right - left + 1
        ):
            return [row[:] for row in grid]
        matching = [color for col, color in markers if left <= col <= right]
        if len(matching) != 1:
            return [row[:] for row in grid]
        for r, c in component:
            output[r][c] = matching[0]
    return output
