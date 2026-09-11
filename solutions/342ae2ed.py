def solve(grid):
    h, w = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    from collections import Counter

    counts = Counter(value for row in grid for value in row)
    background = next(value for value in counts if counts[value] == max(counts.values()))
    for color in sorted({value for row in grid for value in row}):
        seen = set()
        comps = []
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
                comps.append(component)
        if len(comps) != 2:
            continue
        first, second = comps
        pairs = [(a, b) for a in first for b in second if abs(a[0] - b[0]) == abs(a[1] - b[1])]
        if not pairs:
            continue
        start, end = min(pairs, key=lambda pair: abs(pair[0][0] - pair[1][0]))
        dr = 1 if end[0] > start[0] else -1
        dc = 1 if end[1] > start[1] else -1
        row, col = (start[0] + dr, start[1] + dc)
        while (row, col) != end:
            if output[row][col] == background or color == 0:
                output[row][col] = color
            row += dr
            col += dc
    return output
