def solve(grid):
    array = grid
    h, w = len(array), len(array[0])
    colors = {v for row in array for v in row if v}
    for color in colors:
        pos = [(r, c) for r in range(h) for c in range(w) if array[r][c] == color]
        if len(pos) != 4:
            continue
        top, left = min(r for r, c in pos), min(c for r, c in pos)
        bottom, right = max(r for r, c in pos), max(c for r, c in pos)
        if (
            set(pos) != {(top, left), (top, right), (bottom, left), (bottom, right)}
            or bottom - top < 2
            or right - left < 2
        ):
            continue
        outside = [row[:] for row in array]
        for r in range(top, bottom + 1):
            for c in range(left, right + 1):
                outside[r][c] = 0
        mp = [(r, c) for r in range(h) for c in range(w) if outside[r][c]]
        if not mp:
            continue
        mt, ml = min(r for r, c in mp), min(c for r, c in mp)
        mb, mr = max(r for r, c in mp), max(c for r, c in mp)
        motif = [row[ml : mr + 1] for row in outside[mt : mb + 1]]
        if (mb - mt + 1, mr - ml + 1) != (bottom - top - 1, right - left - 1):
            continue
        framed = [row[left : right + 1] for row in array[top : bottom + 1]]
        lv = [framed[r][0] for r in range(1, len(framed) - 1)]
        rv = [framed[r][-1] for r in range(1, len(framed) - 1)]
        lc = max(set(lv), key=lv.count)
        rc = max(set(rv), key=rv.count)
        lp = [c for r in range(len(motif)) for c in range(len(motif[0])) if motif[r][c] == lc]
        rp = [c for r in range(len(motif)) for c in range(len(motif[0])) if motif[r][c] == rc]
        if lc != rc and lp and rp and sum(lp) / len(lp) > sum(rp) / len(rp):
            motif = [row[::-1] for row in motif]
        for r in range(1, len(framed) - 1):
            framed[r][1:-1] = motif[r - 1]
        return framed
    return [row[:] for row in array]
