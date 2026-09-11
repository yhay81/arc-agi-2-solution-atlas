from collections import Counter, defaultdict


def get_components(grid):
    height, width = len(grid), len(grid[0])
    owner = [[-1] * width for _ in range(height)]
    seen = [[False] * width for _ in range(height)]
    components = []
    for r in range(height):
        for c in range(width):
            if grid[r][c] in (0, 2) or seen[r][c]:
                continue
            color = grid[r][c]
            stack = [(r, c)]
            seen[r][c] = True
            cells = []
            while stack:
                row, col = stack.pop()
                cells.append((row, col))
                owner[row][col] = len(components)
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, col + dc
                    if (
                        0 <= nr < height
                        and 0 <= nc < width
                        and not seen[nr][nc]
                        and grid[nr][nc] == color
                    ):
                        seen[nr][nc] = True
                        stack.append((nr, nc))
            rows = [r for r, _ in cells]
            cols = [c for _, c in cells]
            components.append(
                {
                    "color": color,
                    "cells": cells,
                    "bbox": (min(rows), max(rows), min(cols), max(cols)),
                }
            )
    return components, owner


def get_connectors(grid, owner):
    height, width = len(grid), len(grid[0])
    connectors = defaultdict(list)
    for r in range(height):
        for c in range(width):
            if grid[r][c] != 2:
                continue
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < height and 0 <= nc < width and owner[nr][nc] != -1:
                    connectors[owner[nr][nc]].append(((r, c), (-dr, -dc)))
                    break
    return connectors


def build_edges(connectors):
    edges = defaultdict(dict)
    ids = list(connectors)
    for index, first in enumerate(ids):
        for second in ids[index + 1 :]:
            matches = Counter()
            for point_a, direction_a in connectors[first]:
                for point_b, direction_b in connectors[second]:
                    if direction_a == (-direction_b[0], -direction_b[1]):
                        delta = point_a[0] - point_b[0], point_a[1] - point_b[1]
                        matches[delta] += 1
            if matches:
                delta, count = max(
                    matches.items(), key=lambda item: (item[1], -abs(item[0][0]) - abs(item[0][1]))
                )
                if count >= 2:
                    edges[first][second] = delta
                    edges[second][first] = -delta[0], -delta[1]
    return edges


def solve(grid):
    height, width = len(grid), len(grid[0])
    components, owner = get_components(grid)
    connectors = get_connectors(grid, owner)
    door = -1
    best_area = -1
    for index, component in enumerate(components):
        top, bottom, left, right = component["bbox"]
        area = (bottom - top + 1) * (right - left + 1)
        if (
            len(component["cells"]) == area
            and min(bottom - top + 1, right - left + 1) >= 3
            and area > best_area
        ):
            door, best_area = index, area
    if door < 0:
        raise ValueError("Door component not found")

    edges = build_edges(connectors)
    translations = {door: (0, 0)}
    while len(translations) < len(components):
        changed = True
        while changed:
            changed = False
            for source in list(translations):
                for target, delta in edges.get(source, {}).items():
                    candidate = (
                        translations[source][0] + delta[0],
                        translations[source][1] + delta[1],
                    )
                    if target not in translations:
                        translations[target] = candidate
                        changed = True
        if len(translations) == len(components):
            break

        placed = {
            (r + translations[index][0], c + translations[index][1])
            for index in translations
            for r, c in components[index]["cells"]
        }
        known = [
            ((r + translations[index][0], c + translations[index][1]), direction)
            for index in translations
            for (r, c), direction in connectors[index]
        ]
        known = [
            (point, direction)
            for point, direction in known
            if sum(point == p for p, _ in known) == 1
        ]
        known_positions = {point for point, _ in known}
        added = False
        for index, component in enumerate(components):
            if index in translations:
                continue
            options = []
            for (r, c), _ in connectors[index]:
                for (target_r, target_c), _ in known:
                    dy, dx = target_r - r, target_c - c
                    shifted = {(row + dy, col + dx) for row, col in component["cells"]}
                    if shifted & placed or any(
                        not (0 <= row < height and 0 <= col < width) for row, col in shifted
                    ):
                        continue
                    matches = sum(
                        (row + dy, col + dx) in known_positions
                        for (row, col), _ in connectors[index]
                    )
                    options.append((matches, -abs(dy) - abs(dx), dy, dx))
            if options:
                _, _, dy, dx = max(options)
                translations[index] = (dy, dx)
                added = True
                break
        if not (added):
            raise ValueError("task assumptions are not satisfied")

    output = [[0] * width for _ in range(height)]
    for index, component in enumerate(components):
        dy, dx = translations[index]
        for r, c in component["cells"]:
            output[r + dy][c + dx] = component["color"]
    for index, points in connectors.items():
        dy, dx = translations[index]
        for (r, c), _ in points:
            output[r + dy][c + dx] = 2
    return output
