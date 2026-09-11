import heapq as heapq
import itertools as itertools


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    out = [row[:] for row in a]
    h, w = len(a), len(a[0])
    for color in {v for row in a for v in row} - {1, 8}:
        points = [(r, c) for r in range(h) for c in range(w) if a[r][c] == color]
        n = len(points)
        if n < 2:
            continue
        index = {p: i for i, p in enumerate(points)}
        full = (1 << n) - 1
        queue = []
        dist = {}
        parent = {}
        counter = itertools.count()
        for p, i in index.items():
            state = (*p, 4, 1 << i)
            dist[state] = (0, 0)
            heapq.heappush(queue, (0, 0, next(counter), state))
            parent[state] = None
        final = None
        while queue:
            steps, turns, _, state = heapq.heappop(queue)
            if dist[state] != (steps, turns):
                continue
            r, c, d, mask = state
            if mask == full:
                final = state
                break
            for nd, (dy, dx) in enumerate([(1, 0), (-1, 0), (0, 1), (0, -1)]):
                y, x = (r + dy, c + dx)
                if not (0 <= y < h and 0 <= x < w) or a[y][x] not in (1, color):
                    continue
                bits = mask | (1 << index[y, x] if (y, x) in index else 0)
                ns = (y, x, nd, bits)
                cost = (steps + 1, turns + (d != 4 and d != nd))
                if cost < dist.get(ns, (10**9, 10**9)):
                    dist[ns] = cost
                    parent[ns] = state
                    heapq.heappush(queue, (*cost, next(counter), ns))
        if not (final):
            raise ValueError("task assumptions are not satisfied")
        while final is not None:
            r, c, d, mask = final
            out[r][c] = color
            final = parent[final]
    return out
