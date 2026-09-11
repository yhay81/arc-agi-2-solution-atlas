def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    parts = []
    for color in {v for row in a for v in row if v}:
        rem = {(r, c) for r in range(h) for c in range(w) if a[r][c] == color}
        while rem:
            s = rem.pop()
            comp = {s}
            q = [s]
            while q:
                r, c = q.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    p = (r + dr, c + dc)
                    if p in rem:
                        rem.remove(p)
                        comp.add(p)
                        q.append(p)
            tips = sorted(
                (
                    p
                    for p in comp
                    if sum(
                        (p[0] + dr, p[1] + dc) in comp
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
                    )
                    <= 1
                ),
                key=lambda p: p[1],
            )
            if not (len(tips) == 2):
                raise ValueError("task assumptions are not satisfied")
            left = min(c for _, c in comp)
            parts.append((left, comp, tips, max(c for _, c in comp) - left + 1, color))
    parts.sort()
    placed = []
    xoff = 0
    end = None
    for left, comp, tips, width, color in parts:
        dy = 0 if end is None else end - tips[0][0]
        cells = {(r + dy, c + xoff - left) for r, c in comp}
        placed.append((cells, color))
        end = tips[1][0] + dy
        xoff += width
    ymin = min(r for cells, _ in placed for r, _ in cells)
    ymax = max(r for cells, _ in placed for r, _ in cells)
    shift = max(0, -ymin) - max(0, ymax - h + 1)
    out = [[0] * xoff for _ in range(h)]
    for cells, color in placed:
        for r, c in cells:
            if 0 <= r + shift < h:
                out[r + shift][c] = color
    return out
