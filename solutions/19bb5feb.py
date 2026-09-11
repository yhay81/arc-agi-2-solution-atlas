from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    nonzero = [value for row in grid for value in row if value]
    if not nonzero:
        return [row[:] for row in grid]
    counts = Counter(nonzero)
    frame = counts.most_common(1)[0][0]
    frame_positions = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == frame]
    if len(frame_positions) < 8:
        return [row[:] for row in grid]
    top, left = min(r for r, _ in frame_positions), min(c for _, c in frame_positions)
    bottom, right = max(r for r, _ in frame_positions), max(c for _, c in frame_positions)
    if bottom - top < 4 or right - left < 4:
        return [row[:] for row in grid]
    output = [[0, 0], [0, 0]]
    center_row, center_col = (top + bottom) / 2, (left + right) / 2
    for color in sorted(counts):
        if color == frame:
            continue
        seen = set()
        for r in range(h):
            for c in range(w):
                if grid[r][c] != color or (r, c) in seen:
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
                            and grid[nr][nc] == color
                            and (nr, nc) not in seen
                        ):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
                row_center = sum(r for r, _ in component) / len(component)
                col_center = sum(c for _, c in component) / len(component)
                output[0 if row_center < center_row else 1][0 if col_center < center_col else 1] = (
                    color
                )
    return output
