from itertools import pairwise, product


def _find_tiles(grid, background):
    height, width = len(grid), len(grid[0])
    tiles = []
    for frame in sorted({value for row in grid for value in row} - {background}):
        seen = set()
        for start_row in range(height):
            for start_col in range(width):
                if grid[start_row][start_col] != frame or (start_row, start_col) in seen:
                    continue
                stack = [(start_row, start_col)]
                seen.add((start_row, start_col))
                component = []
                while stack:
                    row, col = stack.pop()
                    component.append((row, col))
                    for neighbor in (
                        (row - 1, col),
                        (row + 1, col),
                        (row, col - 1),
                        (row, col + 1),
                    ):
                        if (
                            0 <= neighbor[0] < height
                            and 0 <= neighbor[1] < width
                            and grid[neighbor[0]][neighbor[1]] == frame
                            and neighbor not in seen
                        ):
                            seen.add(neighbor)
                            stack.append(neighbor)
                if len(component) < 4:
                    continue
                rows, cols = zip(*component)
                top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)
                if bottom - top < 2 or right - left < 2:
                    continue
                interior = [
                    grid[row][col]
                    for row in range(top + 1, bottom)
                    for col in range(left + 1, right)
                ]
                marker_values = {value for value in interior if value not in (background, frame)}
                if len(marker_values) != 1 or any(
                    value not in (frame, *marker_values) for value in interior
                ):
                    continue
                perimeter = {
                    (row, col) for row in (top, bottom) for col in range(left, right + 1)
                } | {(row, col) for col in (left, right) for row in range(top, bottom + 1)}
                full_panel = all(
                    grid[row][col] != background
                    for row in range(top, bottom + 1)
                    for col in range(left, right + 1)
                )
                if not (perimeter <= set(component) or full_panel):
                    continue
                marker = next(iter(marker_values))
                tiles.append(
                    {
                        "top": top,
                        "bottom": bottom,
                        "left": left,
                        "right": right,
                        "color": marker,
                        "frame": frame,
                        "marker_cells": [
                            (row, col)
                            for row in range(top + 1, bottom)
                            for col in range(left + 1, right)
                            if grid[row][col] == marker
                        ],
                    }
                )
    return tiles


def _find_guide(grid, background, tiles):
    height, width = len(grid), len(grid[0])
    occupied = {
        (row, col)
        for tile in tiles
        for row in range(tile["top"], tile["bottom"] + 1)
        for col in range(tile["left"], tile["right"] + 1)
    }
    frames = {tile["frame"] for tile in tiles}
    candidates = []
    for axis, major, minor in (("row", height, width), ("column", width, height)):
        for index in range(major):
            points = [
                point
                for point in range(minor)
                if ((index, point) if axis == "row" else (point, index)) not in occupied
                and (value := grid[index][point] if axis == "row" else grid[point][index])
                != background
                and value not in frames
            ]
            if len(points) >= 2:
                candidates.append((len(points), axis, index, points))
    if not candidates:
        return None
    _, axis, index, points = max(candidates, key=lambda item: item[0])
    return [grid[index][point] if axis == "row" else grid[point][index] for point in sorted(points)]


def _select_tiles(tiles, sequence):
    by_color = {}
    for index, tile in enumerate(tiles):
        by_color.setdefault(tile["color"], []).append(index)
    if any(color not in by_color for color in sequence):
        return None
    best = None
    for assignment in product(*(by_color[color] for color in sequence)):
        if len(set(assignment)) != len(assignment):
            continue
        aligned = sum(
            (
                tiles[first]["top"] == tiles[second]["top"]
                and tiles[first]["bottom"] == tiles[second]["bottom"]
            )
            or (
                tiles[first]["left"] == tiles[second]["left"]
                and tiles[first]["right"] == tiles[second]["right"]
            )
            for first, second in pairwise(assignment)
        )
        candidate = aligned, -len(sequence), assignment
        if best is None or candidate > best:
            best = candidate
    return best[2] if best is not None and best[0] == len(sequence) - 1 else None


def _connect_tiles(grid, background, tiles, sequence, assignment):
    output = [row[:] for row in grid]
    for first, second, color in zip(assignment[:-1], assignment[1:], sequence[:-1], strict=True):
        source, target = tiles[first], tiles[second]
        if source["top"] == target["top"] and source["bottom"] == target["bottom"]:
            if source["right"] < target["left"]:
                left, right = source["right"] + 1, target["left"] - 1
            else:
                left, right = target["right"] + 1, source["left"] - 1
            rows = {row for row, _ in source["marker_cells"]}
            for row in rows:
                for col in range(left, right + 1):
                    if output[row][col] == background:
                        output[row][col] = color
        elif source["left"] == target["left"] and source["right"] == target["right"]:
            if source["bottom"] < target["top"]:
                top, bottom = source["bottom"] + 1, target["top"] - 1
            else:
                top, bottom = target["bottom"] + 1, source["top"] - 1
            columns = {col for _, col in source["marker_cells"]}
            for row in range(top, bottom + 1):
                for col in columns:
                    if output[row][col] == background:
                        output[row][col] = color
    return output


def solve(grid):
    if not grid or not grid[0]:
        return [row[:] for row in grid]
    values = {value for row in grid for value in row}
    background = max(values, key=lambda value: sum(row.count(value) for row in grid))
    tiles = _find_tiles(grid, background)
    if len(tiles) < 2 or (sequence := _find_guide(grid, background, tiles)) is None:
        return [row[:] for row in grid]
    assignment = _select_tiles(tiles, sequence)
    return (
        [row[:] for row in grid]
        if assignment is None
        else _connect_tiles(grid, background, tiles, sequence, assignment)
    )
