def solve(grid):
    h, w = len(grid), len(grid[0])
    source = [row[:] for row in grid]
    nodes = []
    for r in range(h):
        for c in range(w):
            arms = [
                (rr, cc)
                for rr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
                if 0 <= rr < h and 0 <= cc < w
            ]
            if len(arms) < 3 or len({source[rr][cc] for rr, cc in arms}) != 1:
                continue
            color, center = source[arms[0][0]][arms[0][1]], source[r][c]
            if color in (0, 5) or center in (0, 5):
                continue
            box = [
                (rr, cc)
                for rr in range(max(0, r - 1), min(h, r + 2))
                for cc in range(max(0, c - 1), min(w, c + 2))
            ]
            if any(source[rr][cc] not in (0, color, center) for rr, cc in box):
                continue
            nodes.append((color, center, (r, c), {p for p in box if source[p[0]][p[1]] != 0}))
    road = {(r, c) for r in range(h) for c in range(w) if source[r][c] == 5}
    ends = []
    for r, c in road:
        neighbors = []
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if not (dr or dc):
                    continue
                q = (r + dr, c + dc)
                if q in road and not (dr and dc and ((r + dr, c) in road or (r, c + dc) in road)):
                    neighbors.append(q)
        if len(neighbors) == 1:
            ends.append((r, c))
    if not (len(ends) == 2):
        raise ValueError("task assumptions are not satisfied")
    adjacent = []
    for r, c in ends:
        candidates = [
            i
            for i, (_, center, _, mask) in enumerate(nodes)
            if any(color == center for color, _, _, _ in nodes)
            and any(max(abs(r - rr), abs(c - cc)) == 1 for rr, cc in mask)
        ]
        distances = [(nodes[i][2][0] - r) ** 2 + (nodes[i][2][1] - c) ** 2 for i in candidates]
        best = min(distances)
        adjacent.append([i for i, distance in zip(candidates, distances) if distance == best])
    assignments = [(i, j) for i in adjacent[0] for j in adjacent[1] if i != j]
    sets = {tuple(sorted(pair)) for pair in assignments}
    if not (len(sets) == 1):
        raise ValueError("task assumptions are not satisfied")
    out = [row[:] for row in source]
    for _, _, _, mask in nodes:
        for r, c in mask:
            out[r][c] = 0
    keep = next(iter(sets))
    for index in keep:
        color, center, _, mask = nodes[index]
        donors = [node for node in nodes if node[0] == center]
        if not (len(donors) == 1):
            raise ValueError("task assumptions are not satisfied")
        for r, c in mask:
            out[r][c] = source[r][c]
        r, c = nodes[index][2]
        out[r][c] = donors[0][1]
    return out
