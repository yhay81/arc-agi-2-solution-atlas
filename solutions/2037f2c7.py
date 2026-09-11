def solve(grid):
    height, width = len(grid), len(grid[0])
    remaining = {(r, c) for r in range(height) for c in range(width) if grid[r][c]}
    objects = []
    while remaining:
        stack = [remaining.pop()]
        cells = set(stack)
        while stack:
            r, c = stack.pop()
            for cell in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if cell in remaining:
                    remaining.remove(cell)
                    cells.add(cell)
                    stack.append(cell)
        top = min(r for r, _ in cells)
        bottom = max(r for r, _ in cells)
        left = min(c for _, c in cells)
        right = max(c for _, c in cells)
        objects.append([row[left : right + 1] for row in grid[top : bottom + 1]])
    a, b = objects
    difference = [[x != y for x, y in zip(arow, brow)] for arow, brow in zip(a, b)]
    rows = [r for r, row in enumerate(difference) if any(row)]
    cols = [c for c in range(len(difference[0])) if any(row[c] for row in difference)]
    return [
        [8 if cell else 0 for cell in row[cols[0] : cols[-1] + 1]]
        for row in difference[rows[0] : rows[-1] + 1]
    ]
