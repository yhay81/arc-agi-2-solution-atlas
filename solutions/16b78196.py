def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def components(g, background=0, diagonal=False, mono=True):
    unseen = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != background}
    out = []
    while unseen:
        p = min(unseen)
        unseen.remove(p)
        q = [p]
        cells = []
        for r, c in q:
            cells.append((r, c))
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if not (dr or dc) or (not diagonal and dr and dc):
                        continue
                    n = (r + dr, c + dc)
                    if n in unseen and (not mono or g[n[0]][n[1]] == g[r][c]):
                        unseen.remove(n)
                        q.append(n)
        out.append(cells)
    return out


def solve(grid):
    g = grid
    return_candidates = False
    g = [row[:] for row in g]
    objects = components(g, 0, False, False)
    beam = max(objects, key=len)
    a, b, c, d = bbox(beam)
    transpose = b - a > d - c
    if transpose:
        g = [list(row) for row in zip(*g)]
        objects = components(g, 0, False, False)
        beam = max(objects, key=len)
    h, w = (len(g), len(g[0]))
    pieces = []
    for obj in objects:
        if obj == beam:
            continue
        a, b, c, d = bbox(obj)
        pts = {(r - a, col - c): g[r][col] for r, col in obj}
        width = d - c + 1
        mins = [min((r for r, col in pts if col == cc)) for cc in range(width)]
        maxs = [max((r for r, col in pts if col == cc)) for cc in range(width)]
        if any(
            sum((col == cc for r, col in pts)) != maxs[cc] - mins[cc] + 1 for cc in range(width)
        ):
            raise ValueError("Piece has a vertical hole")
        pieces.append((pts, width, mins, maxs))
    initial = {(r, c): g[r][c] for r, c in beam}
    solutions = []
    seen = set()

    def search(remaining, paint, ports=()):
        state = (remaining, tuple(sorted(paint.items())))
        if state in seen or len(solutions) > 100:
            return
        seen.add(state)
        if len(seen) > 40000:
            raise ValueError("Search budget")
        if not remaining:
            for col, width, side in ports:
                profile = [
                    (min if side < 0 else max)((r for r, c in paint if c == cc))
                    for cc in range(col, col + width)
                ]
                if len(set(profile)) != 1:
                    return
            solutions.append(paint)
            return
        top = [min((r for r, c in paint if c == col)) for col in range(w)]
        bottom = [max((r for r, c in paint if c == col)) for col in range(w)]
        for i in remaining:
            pts, width, mins, maxs = pieces[i]
            for c in range(w - width + 1):
                for side in (-1, 1):
                    if any(
                        (
                            side == ss
                            and max(c, cc) < min(c + width, cc + ww)
                            and ((c, width) != (cc, ww))
                            for cc, ww, ss in ports
                        )
                    ):
                        continue
                    edge = (top if side < 0 else bottom)[c : c + width]
                    if len(set(edge)) == 1:
                        continue
                    shifts = [
                        edge[k] + side - (maxs[k] if side < 0 else mins[k]) for k in range(width)
                    ]
                    if len(set(shifts)) != 1:
                        continue
                    shift = shifts[0]
                    p = {(r + shift, col + c): v for (r, col), v in pts.items()}
                    if any((r < 0 or r >= h for r, col in p)) or set(p) & set(paint):
                        continue
                    search(
                        tuple(j for j in remaining if j != i),
                        {**paint, **p},
                        ports + ((c, width, side),),
                    )

    search(tuple(range(len(pieces))), initial)
    if return_candidates:
        return [solutions, transpose]
    if len(solutions) != 1:
        raise ValueError(f"Packing solutions: {len(solutions)}")
    out = [[0] * w for _ in range(h)]
    for (r, c), v in solutions[0].items():
        out[r][c] = v
    return [list(row) for row in zip(*out)] if transpose else out
