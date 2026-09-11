def solve(grid):
    a = grid
    a = [row[:] for row in a]
    h, w = len(a), len(a[0])
    mask = [[value == 1 for value in row] for row in a]
    row_counts = [sum(row) for row in mask]
    col_counts = [sum(mask[r][c] for r in range(h)) for c in range(w)]

    def runs(values):
        groups = []
        for value in values:
            if groups and value == groups[-1][-1] + 1:
                groups[-1].append(value)
            else:
                groups.append([value])
        return groups

    hr = max(
        runs([r for r, count in enumerate(row_counts) if count > max(row_counts) * 0.65]), key=len
    )
    vc = max(
        runs([c for c, count in enumerate(col_counts) if count > max(col_counts) * 0.65]), key=len
    )

    def median(values):
        values = sorted(values)
        middle = len(values) // 2
        return int(values[middle] if len(values) % 2 else (values[middle - 1] + values[middle]) / 2)

    hl = median([next(c for c in range(w) if mask[r][c]) for r in hr])
    hh = median([max(c for c in range(w) if mask[r][c]) for r in hr])
    vt = median([next(r for r in range(h) if mask[r][c]) for c in vc])
    vb = median([max(r for r in range(h) if mask[r][c]) for c in vc])
    base = [[False] * w for _ in range(h)]
    for r in range(min(hr), max(hr) + 1):
        for c in range(hl, hh + 1):
            base[r][c] = True
    for r in range(vt, vb + 1):
        for c in range(min(vc), max(vc) + 1):
            base[r][c] = True
    out = [row[:] for row in a]
    for r in range(h):
        for c in range(w):
            extra = mask[r][c]
            if extra == base[r][c]:
                continue
            directions = []
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if extra:
                    nr, nc = r - dr, c - dc
                    if 0 <= nr < h and 0 <= nc < w and base[nr][nc]:
                        directions.append((dr, dc))
                else:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < h and 0 <= nc < w and base[nr][nc]):
                        directions.append((dr, dc))
            if not (len(directions) == 1):
                raise ValueError("task assumptions are not satisfied")
            dr, dc = directions[0]
            axis = 0 if dr else 1
            line_index = c if axis == 0 else r
            indices = [
                i
                for i in range(h if axis == 0 else w)
                if (base[i][line_index] if axis == 0 else base[line_index][i])
            ]
            if extra:
                pr, pc = r - dr, c - dc
                indices = [
                    i
                    for i in range(h if axis == 0 else w)
                    if (base[i][pc] if axis == 0 else base[pr][i])
                ]
            target = [r, c]
            target[axis] = (
                min(indices)
                + max(indices)
                - target[axis]
                + (dr if axis == 0 else dc) * (1 if extra else -1)
            )
            if not (0 <= target[0] < h and 0 <= target[1] < w):
                raise ValueError("task assumptions are not satisfied")
            out[target[0]][target[1]] = 8 if extra else 1
    return out
