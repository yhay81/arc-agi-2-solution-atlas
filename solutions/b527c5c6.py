from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = Counter(value for row in grid for value in row)
    background = counts.most_common(1)[0][0]
    if 2 not in counts:
        return [row[:] for row in grid]
    remaining = {(r, c) for r in range(h) for c in range(w) if grid[r][c] != background}
    components = []
    while remaining:
        seed = min(remaining)
        remaining.remove(seed)
        stack = [seed]
        component = [seed]
        while stack:
            r, c = stack.pop()
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    point = (r + dr, c + dc)
                    if (dr or dc) and point in remaining:
                        remaining.remove(point)
                        stack.append(point)
                        component.append(point)
        components.append(component)
    output = [row[:] for row in grid]
    for component in components:
        markers = [(r, c) for r, c in component if grid[r][c] == 2]
        if len(markers) != 1:
            continue
        marker_row, marker_col = markers[0]
        members = set(component)
        opens = [
            (dr, dc)
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1))
            if (marker_row + dr, marker_col + dc) not in members
            or not (0 <= marker_row + dr < h and 0 <= marker_col + dc < w)
        ]
        if len(opens) != 1:
            continue
        dr, dc = opens[0]
        thickness = (
            max(r for r, _ in component) - min(r for r, _ in component) + 1
            if dr
            else max(c for _, c in component) - min(c for _, c in component) + 1
        )
        for step in range(1, max(h, w)):
            row, col = marker_row + dr * step, marker_col + dc * step
            if not (0 <= row < h and 0 <= col < w):
                break
            for offset in range(-(thickness - 1), thickness):
                tr, tc = row + (offset if dc else 0), col + (offset if dr else 0)
                if 0 <= tr < h and 0 <= tc < w:
                    output[tr][tc] = 2 if offset == 0 else 3
    return output
