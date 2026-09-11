def components(grid, color):
    h, w = len(grid), len(grid[0])
    unseen = {(r, c) for r in range(h) for c in range(w) if grid[r][c] == color}
    out = []
    while unseen:
        start = unseen.pop()
        q = [start]
        cells = []
        for r, c in q:
            cells.append((r, c))
            for p in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if p in unseen:
                    unseen.remove(p)
                    q.append(p)
        out.append(cells)
    return out


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    h, w = len(a), len(a[0])
    out = [row[:] for row in a]
    moves = []
    for color in {v for row in a for v in row if v}:
        for shape in components(a, color):
            if len(shape) < 3:
                continue
            rs = [p[0] for p in shape]
            cs = [p[1] for p in shape]
            r, b, c, d = min(rs), max(rs), min(cs), max(cs)
            if r == b or c == d:
                continue
            corners = [
                p
                for p in ((r, c), (r, d), (b, c), (b, d))
                if a[p[0]][p[1]] == color
                and sum(x == p[0] for x in rs) > 1
                and sum(x == p[1] for x in cs) > 1
            ]
            if len(corners) != 1:
                continue
            marks = [
                (rr, cc)
                for rr in range(r, b + 1)
                for cc in range(c, d + 1)
                if a[rr][cc] not in (0, color)
            ]
            if len(marks) != 1:
                continue
            mark = marks[0]
            key = a[mark[0]][mark[1]]
            targets = [
                (rr, cc)
                for rr in range(h)
                for cc in range(w)
                if a[rr][cc] == key and not (r <= rr <= b and c <= cc <= d)
            ]
            if len(targets) != 1:
                continue
            delta = (targets[0][0] - corners[0][0], targets[0][1] - corners[0][1])
            moves.append((shape + [mark], delta))
    for ps, delta in moves:
        for r, c in ps:
            out[r][c] = 0
    for ps, (dr, dc) in moves:
        for r, c in ps:
            rr, cc = r + dr, c + dc
            if 0 <= rr < h and 0 <= cc < w:
                out[rr][cc] = a[r][c]
    return out
