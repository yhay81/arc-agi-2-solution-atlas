def components(grid, color=2, connectivity=4):
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    if connectivity == 8:
        offsets += [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    unseen = {(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == color}
    groups = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        pending = [start]
        group = []
        while pending:
            r, c = pending.pop()
            group.append((r, c))
            for dr, dc in offsets:
                point = (r + dr, c + dc)
                if point in unseen:
                    unseen.remove(point)
                    pending.append(point)
        groups.append(group)
    return groups


def solve(grid):
    rule = None
    grid = [row[:] for row in grid]
    if rule is None:
        rule = {"source_color": 2, "target_color": 6, "connectivity": 4, "minimum_area": 4}
    out = [row[:] for row in grid]
    for group in components(grid, rule["source_color"], rule["connectivity"]):
        if len(group) >= rule["minimum_area"]:
            for r, c in group:
                out[r][c] = rule["target_color"]
    return out
