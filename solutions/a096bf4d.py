def runs(indices):
    groups = []
    for n in indices:
        if not groups or n != groups[-1][-1] + 1:
            groups.append([])
        groups[-1].append(int(n))
    return groups


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    rs = runs([r for r, row in enumerate(a) if any(v != 0 for v in row)])
    cs = runs([c for c in range(len(a[0])) if any(row[c] != 0 for row in a)])
    out = [row[:] for row in a]
    counts = {}
    for row in a:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    colors = [c for c in sorted(counts, key=counts.get, reverse=True) if c != 0]
    base = set(colors[:2])
    marks = []
    for i, ys in enumerate(rs):
        for j, xs in enumerate(cs):
            for y in range(len(ys)):
                for x in range(len(xs)):
                    value = a[ys[y]][xs[x]]
                    if value not in base and value != 0:
                        marks.append((i, j, y, x, value))
    for i, j, y, x, col in marks:
        for ii, jj, yy, xx, col2 in marks:
            if col != col2 or y != yy or x != xx:
                continue
            if i == ii:
                for cc in range(min(j, jj), max(j, jj) + 1):
                    out[rs[i][y]][cs[cc][x]] = col
            if j == jj:
                for rr in range(min(i, ii), max(i, ii) + 1):
                    out[rs[rr][y]][cs[j][x]] = col
    return out
