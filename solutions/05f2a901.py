def solve(grid):
    h, w = len(grid), len(grid[0])
    twos = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 2]
    eights = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 8]
    if not twos or not eights:
        return [r[:] for r in grid]
    tminr, tmaxr = min(r for r, _ in twos), max(r for r, _ in twos)
    tminc, tmaxc = min(c for _, c in twos), max(c for _, c in twos)
    eminr, emaxr = min(r for r, _ in eights), max(r for r, _ in eights)
    eminc, emaxc = min(c for _, c in eights), max(c for _, c in eights)
    if tmaxc < eminc:
        dr, dc = 0, eminc - tmaxc - 1
    elif emaxc < tminc:
        dr, dc = 0, emaxc - tminc + 1
    elif tmaxr < eminr:
        dr, dc = eminr - tmaxr - 1, 0
    elif emaxr < tminr:
        dr, dc = emaxr - tminr + 1, 0
    else:
        return [r[:] for r in grid]
    out = [[0 if v == 2 else v for v in row] for row in grid]
    for r, c in twos:
        if 0 <= r + dr < h and 0 <= c + dc < w:
            out[r + dr][c + dc] = 2
    return out
