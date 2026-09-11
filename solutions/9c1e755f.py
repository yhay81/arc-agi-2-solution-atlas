def solve(grid):
    a = [list(map(int, row)) for row in grid]
    h, w = len(a), len(a[0]) if a else 0

    def replicate(rows):
        guide = None
        for r, row in enumerate(rows):
            start = 0
            while start < w:
                if row[start] == 0:
                    start += 1
                    continue
                end = start + 1
                while end < w and row[end] == row[start]:
                    end += 1
                if end - start >= 3 and (guide is None or end - start > guide[1] - guide[0] + 1):
                    guide = (start, end - 1, r)
                start = end
        if guide is None:
            return [row[:] for row in rows]
        left, right, guide_row = guide
        out = [row[:] for row in rows]
        for r, row in enumerate(rows):
            if r != guide_row:
                vals = [v for v in row[left : right + 1] if v]
                if vals and len(set(vals)) == 1:
                    out[r][left : right + 1] = [vals[0]] * (right - left + 1)
        return out

    working = replicate(a)
    out = [row[:] for row in working]
    for col in range(w):
        positions = [r for r in range(h) if working[r][col]]
        if len(positions) < 3 or len({working[r][col] for r in positions}) != 1:
            continue
        if positions[-1] - positions[0] + 1 != len(positions):
            continue
        top, bottom = positions[0], positions[-1]
        right_end = next((c for c in range(col + 1, w) if all(a[r][c] == 0 for r in range(h))), w)
        left_start = next(
            (c + 1 for c in range(col - 1, -1, -1) if all(a[r][c] == 0 for r in range(h))), 0
        )
        sides = ((left_start, col), (col + 1, right_end))
        active = [
            [r for r in range(top, bottom + 1) if any(a[r][c] for c in range(start, end))]
            for start, end in sides
        ]
        if not any(active):
            continue
        side = max(
            (i for i in range(2) if active[i]), key=lambda i: (active[i][-1], len(active[i]))
        )
        start, end = sides[side]
        rows = [r for r in range(top, bottom + 1) if any(a[r][c] for c in range(start, end))]
        if not rows:
            continue
        motif_bottom = rows[-1]
        motif_top = motif_bottom
        while motif_top > top and any(a[motif_top - 1][c] for c in range(start, end)):
            motif_top -= 1
        period = motif_bottom - motif_top + 1
        if period > 4:
            continue
        motif = [working[r][start:end] for r in range(motif_top, motif_bottom + 1)]
        for r in range(top, bottom + 1):
            out[r][start:end] = motif[(r - top) % period][:]
        return replicate(out)
    return working
