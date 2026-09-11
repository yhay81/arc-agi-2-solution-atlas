def solve(grid):
    a = grid
    a = [row[:] for row in a]
    out = [row[:] for row in a]
    twos = [(r, c) for r, row in enumerate(a) for c, value in enumerate(row) if value == 2]
    minr, minc = min(r for r, _ in twos), min(c for _, c in twos)
    shape = [(r - minr, c - minc) for r, c in twos]
    sh = max((r for r, c in shape)) + 1
    sw = max((c for r, c in shape)) + 1
    center = (sh // 2, sw // 2)
    center_required = sh % 2 == sw % 2 == 1 and center not in shape
    selected = set()
    for r0 in range(len(a) - sh + 1):
        for c0 in range(len(a[0]) - sw + 1):
            if (sh == 1 and r0 != minr) or (sw == 1 and c0 != minc):
                continue
            if center_required and a[r0 + center[0]][c0 + center[1]] != 5:
                continue
            cells = {(r0 + r, c0 + c) for r, c in shape}
            if all(a[r][c] == 0 for r, c in cells) and not cells & selected:
                selected |= cells
    for point in selected:
        out[point[0]][point[1]] = 2
    return out
