from collections import Counter, deque


def mode(values):
    flat = [v for row in values for v in row] if values and isinstance(values[0], list) else values
    return Counter(flat).most_common(1)[0][0]


def components(mask, diagonal=False):
    unseen = {(r, c) for r, row in enumerate(mask) for c, v in enumerate(row) if v}
    out = []
    offsets = [
        (dr, dc)
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if (dr or dc) and (diagonal or not (dr and dc))
    ]
    while unseen:
        p = min(unseen)
        unseen.remove(p)
        q = [p]
        cells = []
        while q:
            r, c = q.pop()
            cells.append((r, c))
            for dr, dc in offsets:
                n = (r + dr, c + dc)
                if n in unseen:
                    unseen.remove(n)
                    q.append(n)
        out.append(cells)
    return out


def depths(cells, height, width):
    inside = set(cells)
    depth = {}
    queue = deque()
    for row, col in cells:
        if (
            row in (0, height - 1)
            or col in (0, width - 1)
            or any(
                (row + dr, col + dc) not in inside
                for dr in (-1, 0, 1)
                for dc in (-1, 0, 1)
                if dr or dc
            )
        ):
            depth[row, col] = 0
            queue.append((row, col))
    while queue:
        row, col = queue.popleft()
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                neighbor = row + dr, col + dc
                if (dr or dc) and neighbor in inside and neighbor not in depth:
                    depth[neighbor] = depth[row, col] + 1
                    queue.append(neighbor)
    return depth


def solve(grid):
    a = grid
    a = [row[:] for row in a]
    bg = mode(a)
    wall = mode([v for row in a for v in row if v != bg])
    out = [row[:] for row in a]
    for p in components([[v != wall for v in row] for row in a], False):
        dist = depths(p, len(a), len(a[0]))
        markers = {}
        for r, c in p:
            if a[r][c] != bg:
                k = dist[(r, c)]
                if not (k not in markers or markers[k] == a[r][c]):
                    raise ValueError("task assumptions are not satisfied")
                markers[k] = a[r][c]
        if not markers:
            continue
        colors = [markers.get(i, bg) for i in range(max(markers) + 1)]
        for r, c in p:
            out[r][c] = colors[dist[(r, c)] % len(colors)]
    return out
