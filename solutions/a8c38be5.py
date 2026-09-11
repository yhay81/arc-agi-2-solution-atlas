from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])
    nz = [v for row in grid for v in row if v]
    if not nz:
        return [r[:] for r in grid]
    body = Counter(nz).most_common(1)[0][0]
    tiles = {}
    for top in range(h - 2):
        for left in range(w - 2):
            tile = [row[left : left + 3] for row in grid[top : top + 3]]
            if any(v == 0 for row in tile for v in row):
                continue
            accents = {(v) for row in tile for v in row if v != body}
            if len(accents) != 1:
                continue
            pos = [(r, c) for r in range(3) for c in range(3) if tile[r][c] != body]
            slot = (
                round(sum(r for r, _ in pos) / len(pos)),
                round(sum(c for _, c in pos) / len(pos)),
            )
            if slot in tiles or not all(0 <= v < 3 for v in slot):
                return [r[:] for r in grid]
            tiles[slot] = tile
    if len(tiles) != 8 or (1, 1) in tiles:
        return [r[:] for r in grid]
    out = [[body] * 9 for _ in range(9)]
    for (r, c), tile in tiles.items():
        for i in range(3):
            out[3 * r + i][3 * c : 3 * c + 3] = tile[i]
    return out
