def solve(grid):
    return_trace = False
    h, w = (len(grid), len(grid[0]))
    seeds = [(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 3]
    if len(seeds) != 2:
        raise ValueError("Expected exactly two initial green cells")
    a, b = seeds
    if abs(a[0] - b[0]) + abs(a[1] - b[1]) != 1:
        raise ValueError("Green cells must share an edge")

    def inside(p):
        return 0 <= p[0] < h and 0 <= p[1] < w

    starts = []
    for outer, inner in ((a, b), (b, a)):
        d = (inner[0] - outer[0], inner[1] - outer[1])
        behind = (outer[0] - d[0], outer[1] - d[1])
        if not inside(behind):
            starts.append((inner, d))
    if len(starts) != 1:
        raise ValueError("Initial ray orientation is not uniquely anchored at a boundary")
    position, direction = starts[0]
    out = [row[:] for row in grid]
    seen = set()
    turns = []
    painted = []
    while True:
        state = (position, direction)
        if state in seen:
            raise ValueError("Ray entered a cycle")
        seen.add(state)
        r, c = position
        dr, dc = direction
        forward = (r + dr, c + dc)
        if not inside(forward):
            break
        if grid[forward[0]][forward[1]] == 8:
            options = [
                d
                for d in ((-dc, dr), (dc, -dr))
                if inside((r + d[0], c + d[1])) and grid[r + d[0]][c + d[1]] != 8
            ]
            if len(options) != 1:
                raise ValueError(f"Corner is not uniquely determined at {position}: {options}")
            new_direction = options[0]
            turns.append({"at": list(position), "from": list(direction), "to": list(new_direction)})
            direction = new_direction
            continue
        position = forward
        if out[position[0]][position[1]] != 3:
            painted.append(list(position))
        out[position[0]][position[1]] = 3
    trace = {
        "start": list(starts[0][0]),
        "initial_direction": list(starts[0][1]),
        "turns": turns,
        "newly_painted_cells": painted,
        "exit_from": list(position),
        "exit_direction": list(direction),
        "steps_including_green_crossings": len(seen) - len(turns),
    }
    return (out, trace) if return_trace else out
