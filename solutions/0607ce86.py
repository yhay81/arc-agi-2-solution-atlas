from collections import Counter


def dense_indices(lines):
    counts = [sum(value != 0 for value in line) for line in lines]
    levels = sorted(set(counts))
    threshold = max(zip(levels, levels[1:]), key=lambda pair: pair[1] - pair[0])[1]
    return [index for index, count in enumerate(counts) if count >= threshold]


def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    rows = dense_indices(g)
    cols = dense_indices(zip(*g))
    a, b = (min(rows), max(rows))
    c, d = (min(cols), max(cols))
    best = None
    for ph in range(2, (b - a + 1) // 2 + 2):
        for pw in range(2, (d - c + 1) // 2 + 2):
            groups = {}
            for r in range(a, b + 1):
                for col in range(c, d + 1):
                    groups.setdefault(((r - a) % ph, (col - c) % pw), []).append(g[r][col])
            template = {p: Counter(vals).most_common(1)[0][0] for p, vals in groups.items()}
            errors = sum((v != template[p] for p, vals in groups.items() for v in vals))
            candidate = errors, ph * pw, ph, pw, template
            if best is None or candidate[:4] < best[:4]:
                best = candidate
    _, _, ph, pw, template = best
    out = [[0] * w for _ in g]
    trailing_rows = ph - 1 - max((r for (r, c), v in template.items() if v))
    trailing_cols = pw - 1 - max((c for (r, c), v in template.items() if v))
    b = a + (b - a + 1 + trailing_rows) // ph * ph - trailing_rows - 1
    d = c + (d - c + 1 + trailing_cols) // pw * pw - trailing_cols - 1
    for r in range(a, b + 1):
        for col in range(c, d + 1):
            out[r][col] = template[(r - a) % ph, (col - c) % pw]
    return out
