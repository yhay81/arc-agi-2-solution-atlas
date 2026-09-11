def _project(grid):
    h, w = len(grid), len(grid[0])
    counts = [sum(v != 0 for v in row) for row in grid]
    if not any(counts) or counts.count(max(counts)) != 1:
        return [row[:] for row in grid]
    template = grid[counts.index(max(counts))]
    symbols = {v for v in template if v}
    if len(symbols) != 2:
        return [row[:] for row in grid]
    out = [row[:] for row in grid]
    changed = False
    ti = counts.index(max(counts))
    for ri, row in enumerate(grid):
        if ri == ti or not any(row):
            continue
        mapping = {}
        for c, value in enumerate(row):
            if value:
                symbol = template[c]
                if not symbol or (symbol in mapping and mapping[symbol] != value):
                    return [r[:] for r in grid]
                mapping[symbol] = value
        if set(mapping) != symbols or len(set(mapping.values())) != 2:
            return [r[:] for r in grid]
        projected = [mapping.get(value, 0) for value in template]
        if any(row[c] and row[c] != projected[c] for c in range(w)):
            return [r[:] for r in grid]
        out[ri] = projected
        changed = True
    return out if changed else [row[:] for row in grid]


def solve(grid):
    return _project(grid)
