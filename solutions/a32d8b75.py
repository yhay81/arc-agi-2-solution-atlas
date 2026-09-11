def put(g, r, c, v):
    if 0 <= r < len(g) and 0 <= c < len(g[0]):
        g[r][c] = v


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    h, w = (len(g), len(g[0]))
    bars = [c for c in range(w) if all(g[r][c] == 6 for r in range(h))]
    left = bars[0] + 1
    right = bars[-1] if len(bars) > 1 else w
    out = [row[left:right] for row in g]
    strips = [(0, bars[0])] + ([(bars[-1] + 1, w)] if len(bars) > 1 else [])
    for lo, hi in strips:
        strip = [row[lo:hi] for row in g]
        sep = next((r for r, row in enumerate(strip) if all(v == 6 for v in row)))
        occupied = [r for r in range(sep) if any(v != 0 for v in strip[r])]
        runs = []
        for r in occupied:
            if runs and runs[-1][-1] == r - 1:
                runs[-1].append(r)
            else:
                runs.append([r])
        if len(runs) != 2:
            raise ValueError("Expected stamp and macro")

        def cut(rows):
            cols = [c for r in rows for c, v in enumerate(strip[r]) if v != 0]
            return [row[min(cols) : max(cols) + 1] for row in strip[min(rows) : max(rows) + 1]]

        stamp = cut(runs[0])
        macro = cut(runs[1])
        colors = list(set(v for row in stamp for v in row))
        mapping = {colors[0]: colors[1], colors[1]: colors[0]}
        stamp = [[mapping[v] for v in row] for row in stamp]
        frames = [r for r in range(sep, h) if all(v == 6 for v in strip[r])]
        middle = frames[1]
        key = next(
            ((r, c) for r in range(sep + 1, middle) for c, v in enumerate(strip[r]) if v == 4)
        )
        bottom = key[0] > (sep + middle) / 2
        anchorright = key[1] > (hi - lo - 1) / 2
        command = [(r, c) for r in range(middle + 1, h) for c, v in enumerate(strip[r]) if v == 7]
        if len({c for r, c in command}) > 1:
            macro = (
                [list(row) for row in zip(*macro[::-1])]
                if sum((c for r, c in command)) / len(command) > (hi - lo - 1) / 2
                else [list(row) for row in zip(*macro)][::-1]
            )
        elif sum((r for r, c in command)) / len(command) > (middle + h) / 2:
            macro = [row[::-1] for row in macro[::-1]]
        sh, sw = (len(stamp), len(stamp[0]))
        mh, mw = (len(macro) * sh, len(macro[0]) * sw)
        start_r = h - mh if bottom else 0
        start_c = len(out[0]) - mw if anchorright else 0
        for r, row in enumerate(macro):
            for c, v in enumerate(row):
                if v:
                    for rr in range(sh):
                        for cc in range(sw):
                            put(out, start_r + r * sh + rr, start_c + c * sw + cc, stamp[rr][cc])
    return out
