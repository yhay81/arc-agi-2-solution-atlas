def solve(grid):
    a = grid
    n = len(a)
    if n < 3 or any(len(r) != n for r in a):
        return [r[:] for r in a]
    c = n // 2
    marks = [(r, x) for r in range(n) for x in range(n) if a[r][x]]
    if not marks or any(((r - c) % 2 or (x - c) % 2) for r, x in marks):
        return [r[:] for r in a]
    groups = {}
    for r, x in marks:
        rad = max(abs(r - c), abs(x - c))
        if not rad:
            return [q[:] for q in a]
        role = "corner" if abs(r - c) == rad and abs(x - c) == rad else "side"
        groups.setdefault(rad, {"corner": [], "side": []})[role].append(a[r][x])
    out = [r[:] for r in a]
    for rad, roles in groups.items():
        t, b = c - rad, c + rad
        if t < 0 or b >= n:
            return [r[:] for r in a]
        for role, colors in roles.items():
            if colors and (len(set(colors)) != 1):
                return [r[:] for r in a]
            if not colors:
                continue
            color = colors[0]
            if role == "corner":
                for r, x in ((t, t), (t, b), (b, t), (b, b)):
                    out[r][x] = color
            else:
                for x in range(t + 2, b, 2):
                    out[t][x] = out[b][x] = color
                for r in range(t + 2, b, 2):
                    out[r][t] = out[r][b] = color
    return out
