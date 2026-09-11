def solve(grid):
    height, width = len(grid), len(grid[0])
    counts = {}
    for row in grid:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    nodes = []
    owner = [[-1] * width for _ in range(height)]
    source = None
    for row in range(height - 2):
        for col in range(width - 2):
            block = [grid[r][col : col + 3] for r in range(row, row + 3)]
            if any(value == background for line in block for value in line):
                continue
            index = len(nodes)
            nodes.append((row, col, block))
            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    owner[r][c] = index
            even = {block[r][c] for r in range(3) for c in range(3) if (r + c) % 2 == 0}
            odd = {block[r][c] for r in range(3) for c in range(3) if (r + c) % 2}
            if len(even) == len(odd) == 1 and block[0][0] != block[0][1]:
                source = index
    if not (source is not None):
        raise ValueError("task assumptions are not satisfied")

    def adjacent(index):
        row, col, _ = nodes[index]
        points = []
        for r in range(row, row + 3):
            points.extend(((r, col - 1), (r, col + 3)))
        for c in range(col, col + 3):
            points.extend(((row - 1, c), (row + 3, c)))
        return [
            (r, c)
            for r, c in points
            if 0 <= r < height and 0 <= c < width and owner[r][c] < 0 and grid[r][c] != background
        ]

    starts = adjacent(source)
    if not (starts and len({grid[r][c] for r, c in starts}) == 1):
        raise ValueError("task assumptions are not satisfied")
    color = grid[starts[0][0]][starts[0][1]]
    road = {
        (r, c)
        for r in range(height)
        for c in range(width)
        if grid[r][c] == color and owner[r][c] < 0
    }
    gaps = []
    for r, c in road:
        for rr, cc in road:
            if r == rr and cc > c:
                gaps.append(cc - c)
            if c == cc and rr > r:
                gaps.append(rr - r)
    step = min(gaps)
    seen = set(starts)
    stack = list(starts)
    while stack:
        row, col = stack.pop()
        for point in ((row - step, col), (row + step, col), (row, col - step), (row, col + step)):
            if point in road and point not in seen:
                seen.add(point)
                stack.append(point)
    ends = [index for index in range(len(nodes)) if index != source and set(adjacent(index)) & seen]
    if not (len(ends) == 1):
        raise ValueError("task assumptions are not satisfied")
    return [row[:] for row in nodes[ends[0]][2]]
