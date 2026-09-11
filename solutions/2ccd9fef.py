import math as math


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    transpose_grid = lambda g: [list(x) for x in zip(*g)]
    candidates = []
    for transpose in [False, True]:
        z = transpose_grid(a) if transpose else a
        for n in range(3, 7):
            if len(z) % n:
                continue
            size = len(z) // n
            frames = [z[i * size : (i + 1) * size] for i in range(n)]
            base = frames[-1]
            dynamic = {v for row in z for v in row} - {v for row in base for v in row}
            if not dynamic:
                continue
            if all(
                all(
                    f[r][c] == base[r][c] or f[r][c] in dynamic
                    for r in range(size)
                    for c in range(len(z[0]))
                )
                for f in frames[:-1]
            ):
                candidates.append((n, transpose, frames, dynamic))
    if not (candidates):
        raise ValueError("task assumptions are not satisfied")
    n, transpose, frames, dynamic = min(candidates, key=lambda q: q[0])
    o = [row[:] for row in frames[-1]]
    target = n - 1
    for color in dynamic:
        times = [i for i, f in enumerate(frames[:-1]) if any(color in row for row in f)]
        if len(times) < 2:
            continue
        period = math.gcd(*[b - a for a, b in zip(times[:-1], times[1:])])
        t0, t1 = times[-2:]
        if (target - t1) % period:
            continue
        multiplier = (target - t1) / (t1 - t0)
        for r in range(len(o)):
            p = [i for i, v in enumerate(frames[t0][r]) if v == color]
            q = [i for i, v in enumerate(frames[t1][r]) if v == color]
            count = round(len(q) + (len(q) - len(p)) * multiplier)
            if count <= 0 or len(q) == 0:
                continue
            step = math.gcd(*[b - a for a, b in zip(q[:-1], q[1:])]) if len(q) > 1 else 1
            start = round(q[0] + (q[0] - p[0]) * multiplier) if len(p) else int(q[0])
            for c in range(start, start + count * step, step):
                if 0 <= c < len(o[0]):
                    o[r][c] = color
    return transpose_grid(o) if transpose else o
