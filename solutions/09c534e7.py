from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    seen = set()
    for r in range(h):
        for c in range(w):
            if not grid[r][c] or (r, c) in seen:
                continue
            stack = [(r, c)]
            seen.add((r, c))
            component = []
            while stack:
                cr, cc = stack.pop()
                component.append((cr, cc))
                for nr, nc in ((cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)):
                    if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            counts = Counter(grid[r][c] for r, c in component)
            dominant = counts.most_common(1)[0][0]
            markers = [(r, c, grid[r][c]) for r, c in component if grid[r][c] != dominant]
            if not markers:
                continue
            for r, c in component:
                if r == 0 or c == 0 or r == h - 1 or c == w - 1:
                    continue
                if all(
                    grid[nr][nc] != 0 for nr in range(r - 1, r + 2) for nc in range(c - 1, c + 2)
                ):
                    marker = min(markers, key=lambda item: abs(r - item[0]) + abs(c - item[1]))
                    output[r][c] = marker[2]
    return output
