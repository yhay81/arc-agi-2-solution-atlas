def solve(grid):
    g = grid
    shift = next((r for r, row in enumerate(g) if row[0] == 2))
    rows = [row[1:] for row in g]
    return rows[-shift:] + rows[:-shift] if shift else rows
