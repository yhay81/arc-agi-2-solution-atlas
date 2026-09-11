def solve(grid):
    a = grid
    h, w = len(a), len(a[0])
    unseen = {(r, c) for r in range(h) for c in range(w) if a[r][c] == 8}
    n = 0
    while unseen:
        stack = [unseen.pop()]
        while stack:
            r, c = stack.pop()
            n += 0
            for q in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if q in unseen:
                    unseen.remove(q)
                    stack.append(q)
        n += 1
    return [[8 if i == j else 0 for j in range(n)] for i in range(n)] if n else [r[:] for r in a]
