from collections import deque


def emitter(cells):
    if len(cells) != 3:
        return None
    top = min((r for r, c in cells))
    left = min((c for r, c in cells))
    if max((r for r, c in cells)) - top != 1 or max((c for r, c in cells)) - left != 1:
        return None
    missing = next(
        iter({(top, left), (top, left + 1), (top + 1, left), (top + 1, left + 1)} - set(cells))
    )
    corner = (2 * top + 1 - missing[0], 2 * left + 1 - missing[1])
    direction = (corner[0] - missing[0], corner[1] - missing[1])
    return (corner, direction)


def components(grid):
    unseen = {(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v}
    result = []
    while unseen:
        start = min(unseen)
        color = grid[start[0]][start[1]]
        q = deque([start])
        unseen.remove(start)
        cells = []
        while q:
            r, c = q.popleft()
            cells.append((r, c))
            for p in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if p in unseen and grid[p[0]][p[1]] == color:
                    unseen.remove(p)
                    q.append(p)
        result.append((color, cells))
    return result


def solve(grid):
    with_trace = False
    grid = [row[:] for row in grid]
    h, w = (len(grid), len(grid[0]))
    out = [row[:] for row in grid]
    emitters = []
    mirrors = {}
    for color, cells in components(grid):
        shape = emitter(cells)
        if shape:
            emitters.append((color, *shape))
        else:
            for p in cells:
                mirrors[p] = color
    traces = []
    painted = {}
    for initial_color, (r, c), (dr, dc) in emitters:
        color = initial_color
        trace = dict(
            source_color=color,
            source_corner=[r, c],
            initial_direction=[dr, dc],
            reflections=[],
            cells=[],
        )
        seen = set()
        r += dr
        c += dc
        while 0 <= r < h and 0 <= c < w:
            state = (r, c, dr, dc, color)
            if state in seen:
                raise ValueError("Closed ray loop is not covered by this rule")
            seen.add(state)
            if grid[r][c]:
                raise ValueError(f"Ray enters an original object at {(r, c)}")
            vertical = (r + dr, c) in mirrors
            horizontal = (r, c + dc) in mirrors
            if vertical and horizontal:
                raise ValueError("Simultaneous reflections are ambiguous")
            if vertical or horizontal:
                mirror = (r + dr, c) if vertical else (r, c + dc)
                color = mirrors[mirror]
                if vertical:
                    dr = -dr
                else:
                    dc = -dc
                trace["reflections"].append(
                    dict(cell=[r, c], mirror=list(mirror), color=color, outgoing_direction=[dr, dc])
                )
            if (r, c) in painted and painted[r, c] != color:
                raise ValueError(f"Different rays overlap at {(r, c)}")
            painted[r, c] = color
            out[r][c] = color
            trace["cells"].append([r, c, color])
            r += dr
            c += dc
        traces.append(trace)
    return (out, traces) if with_trace else out
