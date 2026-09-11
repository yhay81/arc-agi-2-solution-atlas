from collections import Counter


def rotate(g, k):
    for _ in range(k % 4):
        g = [list(row) for row in zip(*g[::-1])]
    return g


def parse(grid):
    h, w = (len(grid), len(grid[0]))
    arrows = []
    out = [row[:] for row in grid]
    used = set()
    centers = sorted(
        ((r, c) for r in range(h) for c in range(w)), key=lambda p: grid[p[0]][p[1]] != 1
    )
    for r, c in centers:
        arms = [
            (dr, dc)
            for dr, dc in DIRECTIONS
            if 0 <= r + dr < h and 0 <= c + dc < w and (grid[r + dr][c + dc] == 1)
        ]
        if len(arms) != 3:
            continue
        missing = next(p for p in DIRECTIONS if p not in arms)
        direction = (-missing[0], -missing[1])
        symbol = {(r, c)} | {(r + dr, c + dc) for dr, dc in arms}
        if symbol & used:
            continue
        dr, dc = direction
        pr, pc = (-dc, dr)
        around = [grid[r + dr + sign * pr][c + dc + sign * pc] for sign in (-1, 1)]
        source = Counter(around).most_common(1)[0][0]
        arrows.append(
            dict(
                center=[r, c],
                direction=list(direction),
                center_color=grid[r][c],
            )
        )
        used.update(symbol)
        for a, b in symbol:
            out[a][b] = source
    markers = []
    for color, cells in component_list(grid):
        if color != 9 or len(cells) != 5:
            continue
        top = min((r for r, c in cells))
        bottom = max((r for r, c in cells))
        left = min((c for r, c in cells))
        right = max((c for r, c in cells))
        if bottom - top != 2 or right - left != 2:
            continue
        corner_sets = [
            {
                (r, c)
                for r in range(top, bottom + 1)
                for c in range(left, right + 1)
                if r == a or c == b
            }
            for a in (top, bottom)
            for b in (left, right)
        ]
        if set(cells) not in corner_sets:
            continue
        around = [
            grid[a][b]
            for a in range(max(0, top - 1), min(h, bottom + 2))
            for b in range(max(0, left - 1), min(w, right + 2))
            if (a, b) not in cells and grid[a][b] != 1
        ]
        source = Counter(around).most_common(1)[0][0]
        for a, b in cells:
            out[a][b] = source
        markers.append({"cells": cells})
    return (out, arrows, markers)


def component_list(g):
    h, w = (len(g), len(g[0]))
    seen = set()
    out = []
    for r in range(h):
        for c in range(w):
            if (r, c) in seen:
                continue
            color = g[r][c]
            seen.add((r, c))
            queue = [(r, c)]
            cells = []
            while queue:
                a, b = queue.pop()
                cells.append((a, b))
                for da, db in DIRECTIONS:
                    p = (a + da, b + db)
                    if (
                        0 <= p[0] < h
                        and 0 <= p[1] < w
                        and (p not in seen)
                        and (g[p[0]][p[1]] == color)
                    ):
                        seen.add(p)
                        queue.append(p)
            out.append((color, cells))
    return out


DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solve(grid):
    grid = [row[:] for row in grid]
    cleaned, arrows, markers = parse(grid)
    h, w = (len(grid), len(grid[0]))
    regions = component_list(cleaned)
    lookup = {p: i for i, (_, cells) in enumerate(regions) for p in cells}
    assignments = {}
    for arrow in arrows:
        r, c = arrow["center"]
        dr, dc = arrow["direction"]
        source = lookup[r, c]
        a, b = (r + dr, c + dc)
        while 0 <= a < h and 0 <= b < w and (lookup[a, b] == source):
            a += dr
            b += dc
        if not (0 <= a < h and 0 <= b < w):
            continue
        destination = lookup[a, b]
        color = regions[source][0] if arrow["center_color"] == 1 else arrow["center_color"]
        if destination in assignments and assignments[destination] != color:
            raise ValueError("Conflicting destination assignments")
        assignments[destination] = color
    result = [row[:] for row in cleaned]
    for i, color in assignments.items():
        for r, c in regions[i][1]:
            result[r][c] = color
    turns = 0
    if markers:
        if len(markers) != 1:
            raise ValueError("Expected at most one L marker")
        cells = markers[0]["cells"]
        top = min(a for a, _ in cells)
        left = min(b for _, b in cells)
        if not all((top, left + offset) in cells for offset in range(3)):
            raise ValueError("L rotation is verified only for the two top-bar orientations")
        upper_left = (top, left) in cells and (top + 1, left) in cells
        turns = 1 if upper_left else 3
    return rotate(result, turns)
