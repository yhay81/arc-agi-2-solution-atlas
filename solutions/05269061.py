def solve(grid):
    h, w = len(grid), len(grid[0])
    values = sorted({v for row in grid for v in row if v})
    if len(values) < 2:
        return [row[:] for row in grid]
    for period in range(2, len(values) + 1):
        if len(values) != period:
            continue
        for sign in (1, -1):
            for phase in range(period):
                mapping = {}
                valid = True
                for r in range(h):
                    for c in range(w):
                        if not grid[r][c]:
                            continue
                        k = (r + sign * c + phase) % period
                        v = grid[r][c]
                        if k in mapping and mapping[k] != v:
                            valid = False
                            break
                        mapping[k] = v
                    if not valid:
                        break
                if valid and len(mapping) == period:
                    return [
                        [mapping[(r + sign * c + phase) % period] for c in range(w)]
                        for r in range(h)
                    ]
    return [row[:] for row in grid]
