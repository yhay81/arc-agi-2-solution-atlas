def parse_frames(grid):
    height, width = (len(grid), len(grid[0]))
    frames = []
    for cells in black_components(grid):
        top = min((r for r, c in cells))
        bottom = max((r for r, c in cells))
        left = min((c for r, c in cells))
        right = max((c for r, c in cells))
        perimeter = {
            (r, c)
            for r in range(top, bottom + 1)
            for c in range(left, right + 1)
            if r in (top, bottom) or c in (left, right)
        }
        if set(cells) != perimeter or bottom - top < 2 or right - left < 2:
            raise ValueError("Black component is not a rectangular frame")
        sides = [
            ((-1, 0), [(top - 1, c) for c in range(left, right + 1)]),
            ((1, 0), [(bottom + 1, c) for c in range(left, right + 1)]),
            ((0, -1), [(r, left - 1) for r in range(top, bottom + 1)]),
            ((0, 1), [(r, right + 1) for r in range(top, bottom + 1)]),
        ]
        attached = [
            (d, points)
            for d, points in sides
            if all((0 <= r < height and 0 <= c < width and (grid[r][c] == 9) for r, c in points))
        ]
        if len(attached) != 1:
            raise ValueError("Expected one attached brown side")
        (dr, dc), line = attached[0]
        distance = None
        for step in range(1, max(height, width)):
            shifted = [(r + step * dr, c + step * dc) for r, c in line]
            if not all((0 <= r < height and 0 <= c < width for r, c in shifted)):
                break
            if all((grid[r][c] == 9 for r, c in shifted)):
                distance = step
                break
        if distance is None:
            raise ValueError("No parallel brown destination")
        gray = [
            (r, c)
            for r in range(top + 1, bottom)
            for c in range(left + 1, right)
            if grid[r][c] == 5
        ]
        if any(
            grid[r][c] not in (5, 7) for r in range(top + 1, bottom) for c in range(left + 1, right)
        ):
            raise ValueError("Unexpected frame interior color")
        if (dr, dc) == (-1, 0):
            key = lambda p: (p[0], p[1])
        elif (dr, dc) == (0, 1):
            key = lambda p: (-p[1], p[0])
        elif (dr, dc) == (1, 0):
            key = lambda p: (-p[0], -p[1])
        else:
            key = lambda p: (p[1], -p[0])
        gray.sort(key=key)
        steps = min(distance, len(gray))
        frames.append(
            {
                "bounds": [top, left, bottom, right],
                "direction": [dr, dc],
                "attached_line": line,
                "destination_distance": distance,
                "gray_before": len(gray),
                "movement_steps": steps,
                "recolored_original_cells": gray[:steps],
            }
        )
    return frames


def black_components(grid):
    unseen = {(r, c) for r, row in enumerate(grid) for c, v in enumerate(row) if v == 0}
    components = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        queue = [start]
        cells = []
        while queue:
            r, c = queue.pop()
            cells.append((r, c))
            for p in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if p in unseen:
                    unseen.remove(p)
                    queue.append(p)
        components.append(cells)
    return components


def solve(grid):
    return_trace = False
    grid = [row[:] for row in grid]
    frames = parse_frames(grid)
    out = [row[:] for row in grid]
    payloads = []
    for frame in frames:
        top, left, bottom, right = frame["bounds"]
        converted = {tuple(p) for p in frame["recolored_original_cells"]}
        pixels = {
            (r, c): 7 if (r, c) in converted else grid[r][c]
            for r in range(top, bottom + 1)
            for c in range(left, right + 1)
        }
        pixels.update({tuple(p): 9 for p in frame["attached_line"]})
        payloads.append(pixels)
        for r, c in pixels:
            out[r][c] = 6
    for frame, pixels in zip(frames, payloads):
        dr, dc = frame["direction"]
        steps = frame["movement_steps"]
        for (r, c), color in pixels.items():
            out[r + steps * dr][c + steps * dc] = color
    return (out, frames) if return_trace else out
