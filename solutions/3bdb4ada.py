def solve(grid):
    array = grid
    h, w = len(array), len(array[0])
    unseen = {(r, c) for r in range(h) for c in range(w) if array[r][c]}
    comps = []
    while unseen:
        stack = [unseen.pop()]
        p = []
        while stack:
            r, c = stack.pop()
            p.append((r, c))
            for q in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if q in unseen:
                    unseen.remove(q)
                    stack.append(q)
        comps.append(p)
    out = [r[:] for r in array]
    for p in comps:
        rows = [r for r, c in p]
        cols = [c for r, c in p]
        top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)
        if (
            bottom - top + 1 != 3
            or len({array[r][c] for r, c in p}) != 1
            or len(p) != 3 * (right - left + 1)
        ):
            return [r[:] for r in array]
        for c in range(left + 1, right + 1, 2):
            out[top + 1][c] = 0
    return out
