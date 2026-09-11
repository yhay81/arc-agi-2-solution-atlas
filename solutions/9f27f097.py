from collections import Counter


def solve(grid):
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    unseen = {(r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 0}
    groups = []
    while unseen:
        pending = [unseen.pop()]
        group = []
        while pending:
            r, c = pending.pop()
            group.append((r, c))
            for point in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if point in unseen:
                    unseen.remove(point)
                    pending.append(point)
        groups.append(group)
    target = max(groups, key=len)
    top = min(r for r, _ in target)
    left, right = min(c for _, c in target), max(c for _, c in target)
    motif = [
        (r, c)
        for r, row in enumerate(grid)
        for c, value in enumerate(row)
        if value not in (0, background)
    ]
    mt, mb = min(r for r, _ in motif), max(r for r, _ in motif)
    ml, mr = min(c for _, c in motif), max(c for _, c in motif)
    patch = [row[ml : mr + 1][::-1] for row in grid[mt : mb + 1]]
    output = [row[:] for row in grid]
    for r, row in enumerate(patch):
        output[top + r][left : right + 1] = row
    return output
