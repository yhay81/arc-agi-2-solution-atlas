def solve(grid):
    rows = [row[:] for row in grid]
    active = [i for i, row in enumerate(rows) if any(row)]
    if len(active) < 2 or active[-1] - active[0] + 1 != len(active):
        return rows
    motif = rows[active[0] : active[-1] + 1]
    return [motif[(i - active[0]) % len(motif)][:] for i in range(len(rows))]
