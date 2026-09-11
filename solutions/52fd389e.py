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
            if not component:
                continue
            counts = Counter(grid[row][col] for row, col in component)
            values = sorted(counts)
            if len(values) < 2:
                continue
            marker = min(values, key=lambda value: counts[value])
            thickness = counts[marker]
            top = min((row for row, _ in component)) - thickness
            bottom = max((row for row, _ in component)) + thickness
            left = min((col for _, col in component)) - thickness
            right = max((col for _, col in component)) + thickness
            clipped_top, clipped_bottom = max(0, top), min(h - 1, bottom)
            clipped_left, clipped_right = max(0, left), min(w - 1, right)
            if clipped_top <= clipped_bottom and clipped_left <= clipped_right:
                for row in range(clipped_top, clipped_bottom + 1):
                    output[row][clipped_left : clipped_right + 1] = [marker] * (
                        clipped_right - clipped_left + 1
                    )
                for row, col in component:
                    output[row][col] = grid[row][col]
    return output
