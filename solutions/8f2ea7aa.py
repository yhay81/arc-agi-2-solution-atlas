def _extract_nonzero_tile_kronecker(array):
    positions = [(r, c) for r, row in enumerate(array) for c, v in enumerate(row) if v]
    if not len(positions):
        return [row[:] for row in array]
    top = min(r for r, c in positions)
    left = min(c for r, c in positions)
    bottom = max(r for r, c in positions)
    right = max(c for r, c in positions)
    tile = [row[left : right + 1] for row in array[top : bottom + 1]]
    if len(tile) != len(tile[0]) or len(tile) < 2:
        return [row[:] for row in array]
    n = len(tile)
    return [
        [tile[br][bc] if tile[ar][ac] else 0 for ac in range(n) for bc in range(n)]
        for ar in range(n)
        for br in range(n)
    ]


def solve(grid):
    return _extract_nonzero_tile_kronecker(grid)
