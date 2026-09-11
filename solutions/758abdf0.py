def solve(grid):
    return_trace = False
    height, width = (len(grid), len(grid[0]))
    walls = [
        ("top", (1, 0), [(0, c) for c in range(width)]),
        ("bottom", (-1, 0), [(height - 1, c) for c in range(width)]),
        ("left", (0, 1), [(r, 0) for r in range(height)]),
        ("right", (0, -1), [(r, width - 1) for r in range(height)]),
    ]
    walls = [wall for wall in walls if all((grid[r][c] == 0 for r, c in wall[2]))]
    if len(walls) != 1:
        raise ValueError("Expected exactly one complete black boundary wall")
    side, (dr, dc), wall_cells = walls[0]
    out = [row[:] for row in grid]
    traces = []
    recognized = set(wall_cells)
    for wr, wc in wall_cells:
        ray = []
        r, c = (wr + dr, wc + dc)
        while 0 <= r < height and 0 <= c < width and (grid[r][c] == 8):
            ray.append((r, c))
            r, c = (r + dr, c + dc)
        if not ray:
            continue
        if len(ray) not in (1, 2):
            raise ValueError("Only attached cyan lengths one and two are supported")
        recognized.update(ray)
        for r, c in ray:
            out[r][c] = 7
        if len(ray) == 1:
            destination = [(wr + step * dr, wc + step * dc) for step in (1, 2)]
            color, action = (8, "grow_from_one_to_two")
        else:
            depth = height if dr else width
            destination = [(wr + step * dr, wc + step * dc) for step in (depth - 2, depth - 1)]
            color, action = (0, "fall_to_opposite_edge_and_turn_black")
        for r, c in destination:
            if not (0 <= r < height and 0 <= c < width):
                raise ValueError("Grid is too narrow for the resulting ray")
            out[r][c] = color
        traces.append(
            {
                "wall_cell": [wr, wc],
                "length_before": len(ray),
                "action": action,
                "source_cells": ray,
                "destination_cells": destination,
                "output_color": color,
            }
        )
    if any(
        (
            value != 7 and (r, c) not in recognized
            for r, row in enumerate(grid)
            for c, value in enumerate(row)
        )
    ):
        raise ValueError("Unexpected pixels outside the wall and attached rays")
    trace = {"wall": side, "direction_away_from_wall": [dr, dc], "rays": traces}
    return (out, trace) if return_trace else out
