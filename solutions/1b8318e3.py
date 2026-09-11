def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    seen, frames = set(), []
    for r in range(h):
        for c in range(w):
            if a[r][c] != 5 or (r, c) in seen:
                continue
            stack, cells = [(r, c)], []
            seen.add((r, c))
            while stack:
                x, y = stack.pop()
                cells.append((x, y))
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    p = (x + dx, y + dy)
                    if 0 <= p[0] < h and 0 <= p[1] < w and a[p[0]][p[1]] == 5 and p not in seen:
                        seen.add(p)
                        stack.append(p)
            frames.append(
                (
                    min(x for x, _ in cells),
                    min(y for _, y in cells),
                    max(x for x, _ in cells),
                    max(y for _, y in cells),
                )
            )
    dots = [(r, c) for r in range(h) for c in range(w) if a[r][c] not in (0, 5)]
    out = [[5 if v == 5 else 0 for v in row] for row in a]

    def distance(box, r, c):
        t, l, b, q = box
        return max(t - r, 0, r - b) + max(l - c, 0, c - q)

    for r, c in dots:
        for t, l, b, q in sorted(frames, key=lambda x: (distance(x, r, c), x[0], x[1])):
            rr = t - 1 if r < t else b + 1 if r > b else r
            cc = l - 1 if c < l else q + 1 if c > q else c
            if r > b and c < l and l - c > 1 and r - b > l - c:
                rr, cc = b + 1, l
            if 0 <= rr < h and 0 <= cc < w and out[rr][cc] == 0:
                out[rr][cc] = a[r][c]
                break
    return out
