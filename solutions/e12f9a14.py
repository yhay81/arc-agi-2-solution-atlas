from collections import Counter
from dataclasses import dataclass
from math import gcd

RING = tuple(
    (dr, dc) for dr in range(-1, 3) for dc in range(-1, 3) if dr in (-1, 2) or dc in (-1, 2)
)


@dataclass
class Ray:
    seed: int
    color: int
    row: int
    col: int
    dr: int
    dc: int
    group: int
    phase: int = 0
    done: bool = False


def _find_seeds(grid):
    background = Counter(cell for row in grid for cell in row).most_common(1)[0][0]
    height, width = len(grid), len(grid[0])
    remaining = {(row, col) for row in range(height) for col in range(width)}
    seeds = []
    while remaining:
        start = min(remaining)
        color = grid[start[0]][start[1]]
        remaining.remove(start)
        stack = [start]
        cells = []
        while stack:
            row, col = stack.pop()
            cells.append((row, col))
            for point in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if point in remaining and grid[point[0]][point[1]] == color:
                    remaining.remove(point)
                    stack.append(point)
        rows = [row for row, _ in cells]
        cols = [col for _, col in cells]
        if (
            color != background
            and len(cells) == 4
            and max(rows) - min(rows) == 1
            and max(cols) - min(cols) == 1
        ):
            seeds.append((color, min(rows), min(cols)))
    return background, seeds


def _openings(grid, background, top, left):
    height, width = len(grid), len(grid[0])
    return {
        (dr, dc)
        for dr, dc in RING
        if 0 <= top + dr < height
        and 0 <= left + dc < width
        and grid[top + dr][left + dc] == background
    }


def _is_spurious_notch(openings, offset):
    return offset == (2, 2) and openings == {(-1, 1), (0, -1), (2, 2)}


def _initial_rays(grid, background, seeds, output):
    rays = []
    for seed, (color, top, left) in enumerate(seeds):
        openings = _openings(grid, background, top, left)
        for dr, dc in RING:
            if (dr, dc) not in openings or _is_spurious_notch(openings, (dr, dc)):
                continue
            row, col = top + dr, left + dc
            vr = -1 if dr == -1 else 1 if dr == 2 else 0
            vc = -1 if dc == -1 else 1 if dc == 2 else 0
            rays.append(Ray(seed, color, row, col, vr, vc, len(rays)))
            output[row][col] = color
    return rays


def _trace(ray, height, width):
    points = [(ray.row, ray.col, ray.phase)]
    row, col, phase = points[0]
    while True:
        vertical, horizontal = abs(ray.dr), abs(ray.dc)
        if vertical >= horizontal:
            row += (ray.dr > 0) - (ray.dr < 0)
            phase += horizontal
            if horizontal and phase >= vertical:
                col += (ray.dc > 0) - (ray.dc < 0)
                phase -= vertical
        else:
            col += (ray.dc > 0) - (ray.dc < 0)
            phase += vertical
            if vertical and phase >= horizontal:
                row += (ray.dr > 0) - (ray.dr < 0)
                phase -= horizontal
        if not (0 <= row < height and 0 <= col < width):
            return points
        points.append((row, col, phase))


def _next_collision(active, traces, rays):
    best = None
    for offset, first_index in enumerate(active):
        for second_index in active[:offset]:
            first, second = rays[first_index], rays[second_index]
            if first.group == second.group or first.seed == second.seed:
                continue
            for first_distance, a in enumerate(traces[first_index]):
                for second_distance, b in enumerate(traces[second_index]):
                    if max(abs(a[0] - b[0]), abs(a[1] - b[1])) <= 1:
                        metric = (
                            max(first_distance, second_distance),
                            first_distance + second_distance,
                            first_distance,
                            second_distance,
                            first_index,
                            second_index,
                        )
                        if best is None or metric < best:
                            best = metric
    return best


def _paint(output, background, ray, path):
    for row, col, _ in path:
        if output[row][col] == background:
            output[row][col] = ray.color


def _advance_group(rays, members, traces, distance, output, background):
    for index in members:
        path = traces[index]
        end = min(distance, len(path) - 1)
        _paint(output, background, rays[index], path[1 : end + 1])
        rays[index].row, rays[index].col, rays[index].phase = path[end]


def _merge_groups(rays, active, first_index, second_index):
    first_group, second_group = rays[first_index].group, rays[second_index].group
    members = [index for index in active if rays[index].group in (first_group, second_group)]
    dr = rays[first_index].dr + rays[second_index].dr
    dc = rays[first_index].dc + rays[second_index].dc
    divisor = gcd(abs(dr), abs(dc))
    if divisor:
        dr, dc = dr // divisor, dc // divisor
    group = min(first_group, second_group)
    for index in members:
        ray = rays[index]
        was_axis_aligned = (ray.dr == 0) != (ray.dc == 0)
        ray.group, ray.dr, ray.dc = group, dr, dc
        major, minor = max(abs(dr), abs(dc)), min(abs(dr), abs(dc))
        ray.phase = -minor if was_axis_aligned and 0 < minor < major else 0
        if dr == dc == 0:
            ray.done = True


def solve(grid):
    background, seeds = _find_seeds(grid)
    height, width = len(grid), len(grid[0])
    output = [row[:] for row in grid]
    rays = _initial_rays(grid, background, seeds, output)
    for _ in range(len(rays)):
        active = [index for index, ray in enumerate(rays) if not ray.done]
        traces = {index: _trace(rays[index], height, width) for index in active}
        collision = _next_collision(active, traces, rays)
        if collision is None:
            for index in active:
                _paint(output, background, rays[index], traces[index][1:])
                rays[index].done = True
            break
        _, _, first_distance, second_distance, first, second = collision
        first_members = [index for index in active if rays[index].group == rays[first].group]
        second_members = [index for index in active if rays[index].group == rays[second].group]
        _advance_group(rays, first_members, traces, first_distance, output, background)
        _advance_group(rays, second_members, traces, second_distance, output, background)
        _merge_groups(rays, active, first, second)
    return output
