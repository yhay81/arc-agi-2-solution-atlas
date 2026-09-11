def solve(grid):
    a = [list(map(int, row)) for row in grid]
    h, w = len(a), len(a[0]) if a else 0
    if not h or not w:
        return a
    separators = [c for c in range(w) if all(a[r][c] == 0 for r in range(h))]
    edges = [-1, *separators, w]
    panels = [
        [row[left + 1 : right] for row in a]
        for left, right in zip(edges, edges[1:])
        if right > left + 1
    ]
    if len(panels) < 2 or len({(len(p), len(p[0])) for p in panels}) != 1:
        return a

    def components(panel, bg):
        ph, pw = len(panel), len(panel[0])
        seen, found = set(), []
        for r in range(ph):
            for c in range(pw):
                if panel[r][c] == bg or (r, c) in seen:
                    continue
                stack, part = [(r, c)], []
                seen.add((r, c))
                while stack:
                    y, x = stack.pop()
                    part.append((y, x))
                    for ny, nx in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
                        if (
                            0 <= ny < ph
                            and 0 <= nx < pw
                            and panel[ny][nx] != bg
                            and (ny, nx) not in seen
                        ):
                            seen.add((ny, nx))
                            stack.append((ny, nx))
                found.append(part)
        return found

    backgrounds, objects = [], []
    for panel in panels:
        vals = {v for row in panel for v in row}
        bg = max(vals, key=lambda c: sum(v == c for row in panel for v in row))
        backgrounds.append(bg)
        parts = components(panel, bg)
        objects.append([(r, c, panel[r][c]) for r, c in max(parts, key=len)] if parts else [])
    if len(set(backgrounds)) != 1:
        return a
    bg = backgrounds[0]
    out = [[bg] * len(panels[0][0]) for _ in range(len(panels[0]))]
    occupied = set()
    centre = ((len(out) - 1) / 2, (len(out[0]) - 1) / 2)
    for obj in objects:
        if not obj:
            continue
        original = [(r, c) for r, c, _ in obj]
        mr = sum(r for r, _ in original) / len(original)
        mc = sum(c for _, c in original) / len(original)
        shifts = [
            (dr, dc)
            for dr in range(-len(out) + 1, len(out))
            for dc in range(-len(out[0]) + 1, len(out[0]))
        ]
        shifts.sort(
            key=lambda s: (
                abs(s[0]) + abs(s[1]),
                -((centre[0] - mr) * s[0] + (centre[1] - mc) * s[1]),
                abs(s[0]),
                abs(s[1]),
                s,
            )
        )
        for dr, dc in shifts:
            moved = [(r + dr, c + dc) for r, c in original]
            if all(
                0 <= r < len(out) and 0 <= c < len(out[0]) and (r, c) not in occupied
                for r, c in moved
            ):
                for (r, c, value), (y, x) in zip(obj, moved):
                    out[y][x] = value
                    occupied.add((y, x))
                break
    return out
