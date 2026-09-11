def solve(grid):
    g = grid
    h, w = (len(g), len(g[0]))
    candidates = []
    for py in range(1, h + 1):
        for px in range(1, w + 1):
            phase = {}
            okay = True
            for r, row in enumerate(g):
                for c, v in enumerate(row):
                    if v == 1:
                        continue
                    key = (r % py, c % px)
                    if key in phase and phase[key] != v:
                        okay = False
                        break
                    phase[key] = v
                if not okay:
                    break
            if okay:
                candidates.append((py * px, py, px, phase))
    _, py, px, phase = min(candidates, key=lambda p: p[:3])
    return [[phase.get((r % py, c % px), 1) for c in range(w)] for r in range(h)]
