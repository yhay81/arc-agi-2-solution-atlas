from collections import Counter
from functools import cache


def bbox(cells):
    return (
        min((r for r, c in cells)),
        max((r for r, c in cells)),
        min((c for r, c in cells)),
        max((c for r, c in cells)),
    )


def bg(g):
    return Counter(v for row in g for v in row).most_common(1)[0][0]


def components(g, background=0, diagonal=False, mono=True):
    unseen = {(r, c) for r, row in enumerate(g) for c, v in enumerate(row) if v != background}
    out = []
    while unseen:
        p = min(unseen)
        unseen.remove(p)
        q = [p]
        cells = []
        for r, c in q:
            cells.append((r, c))
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if not (dr or dc) or (not diagonal and dr and dc):
                        continue
                    n = (r + dr, c + dc)
                    if n in unseen and (not mono or g[n[0]][n[1]] == g[r][c]):
                        unseen.remove(n)
                        q.append(n)
        out.append(cells)
    return out


def solve(grid):
    g = grid
    g = [row[:] for row in g]
    background = bg(g)
    objects = components(g, background, True, False)
    if len(objects) != 2:
        raise ValueError("Expected outlined target and colored example")
    target = min(objects, key=lambda o: len({g[r][c] for r, c in o}))
    source = max(objects, key=lambda o: len({g[r][c] for r, c in o}))
    wall = g[target[0][0]][target[0][1]]

    def regions(obj, filled):
        a, b, c, d = bbox(obj)
        member = set(obj)
        grid = [
            [g[r][col] if (r, col) in member else background for col in range(c, d + 1)]
            for r in range(a, b + 1)
        ]
        mask = [[int(v != wall) for v in row] for row in grid]
        parts = components(mask, 0, False, True)
        parts = [
            o
            for o in parts
            if all(
                (r not in (0, len(grid) - 1) and col not in (0, len(grid[0]) - 1) for r, col in o)
            )
        ]
        return (grid, parts)

    template, holes = regions(target, False)
    ref, marks = regions(source, True)
    if len(holes) != len(marks):
        raise ValueError(f"Hole counts {len(holes)} vs {len(marks)}")

    def center(o, grid):
        return (
            sum((r for r, c in o)) / len(o) / len(grid),
            sum((c for r, c in o)) / len(o) / len(grid[0]),
        )

    centers = [center(o, template) for o in holes]
    refs = [center(o, ref) for o in marks]

    @cache
    def match(index, used):
        if index == len(centers):
            return 0, ()
        choices = []
        for other in range(len(refs)):
            if used >> other & 1:
                continue
            suffix_cost, suffix = match(index + 1, used | 1 << other)
            distance = sum((centers[index][axis] - refs[other][axis]) ** 2 for axis in (0, 1))
            choices.append((distance + suffix_cost, (other, *suffix)))
        return min(choices)

    _, pairs = match(0, 0)
    for i, j in enumerate(pairs):
        colors = Counter((ref[r][c] for r, c in marks[j]))
        color = colors.most_common(1)[0][0]
        for r, c in holes[i]:
            template[r][c] = color
    return template
