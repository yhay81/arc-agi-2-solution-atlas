from collections import Counter, deque


def solve(grid):
    height, width = len(grid), len(grid[0])
    background = Counter(value for row in grid for value in row).most_common(1)[0][0]
    seen = [[False] * width for _ in range(height)]
    components = []
    for r in range(height):
        for c in range(width):
            if seen[r][c] or grid[r][c] == background:
                continue
            color = grid[r][c]
            queue = deque([(r, c)])
            seen[r][c] = True
            cells = []
            while queue:
                row, col = queue.popleft()
                cells.append((row, col))
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = row + dr, col + dc
                    if (
                        0 <= nr < height
                        and 0 <= nc < width
                        and not seen[nr][nc]
                        and grid[nr][nc] == color
                    ):
                        seen[nr][nc] = True
                        queue.append((nr, nc))
            rows = [row for row, _ in cells]
            cols = [col for _, col in cells]
            top, bottom, left, right = min(rows), max(rows), min(cols), max(cols)
            components.append(
                {
                    "color": color,
                    "cells": cells,
                    "bbox": (top, bottom, left, right),
                    "height": bottom - top + 1,
                    "width": right - left + 1,
                }
            )

    max_area = max(comp["height"] * comp["width"] for comp in components)
    tiles = [comp for comp in components if comp["height"] * comp["width"] == max_area]
    shapes = [comp for comp in components if comp not in tiles]
    if not tiles or len(tiles) != len(shapes):
        return [row[:] for row in grid]

    min_top = min(comp["bbox"][0] for comp in tiles)
    min_left = min(comp["bbox"][2] for comp in tiles)
    tile_height, tile_width = tiles[0]["height"], tiles[0]["width"]
    for tile in tiles:
        top, _, left, _ = tile["bbox"]
        tile["grid_pos"] = (
            round((top - min_top) / tile_height),
            round((left - min_left) / tile_width),
        )
    tiles.sort(key=lambda comp: comp["grid_pos"])
    rows = max(comp["grid_pos"][0] for comp in tiles) + 1
    cols = max(comp["grid_pos"][1] for comp in tiles) + 1

    by_holes = {}
    for shape in shapes:
        top, bottom, left, right = shape["bbox"]
        pattern = [row[left : right + 1] for row in grid[top : bottom + 1]]
        ph, pw = len(pattern), len(pattern[0])
        outside = [[False] * pw for _ in range(ph)]
        queue = deque()
        for r in range(ph):
            for c in range(pw):
                if r in (0, ph - 1) or c in (0, pw - 1):
                    if pattern[r][c] != shape["color"] and not outside[r][c]:
                        outside[r][c] = True
                        queue.append((r, c))
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < ph
                    and 0 <= nc < pw
                    and pattern[nr][nc] != shape["color"]
                    and not outside[nr][nc]
                ):
                    outside[nr][nc] = True
                    queue.append((nr, nc))
        holes = {
            (r, c)
            for r in range(ph)
            for c in range(pw)
            if pattern[r][c] != shape["color"] and not outside[r][c]
        }
        count = 0
        while holes:
            count += 1
            start = holes.pop()
            queue = [start]
            while queue:
                r, c = queue.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    point = r + dr, c + dc
                    if point in holes:
                        holes.remove(point)
                        queue.append(point)
        by_holes[count] = shape

    assignment = {}
    for index, tile in enumerate(tiles):
        top, bottom, left, right = tile["bbox"]
        count = sum(
            grid[r][c] == background for r in range(top, bottom + 1) for c in range(left, right + 1)
        )
        assignment[index] = by_holes[count]

    output = [[0] * (cols * tile_width) for _ in range(rows * tile_height)]
    for index, tile in enumerate(tiles):
        row_pos, col_pos = tile["grid_pos"]
        top, left = row_pos * tile_height, col_pos * tile_width
        for r in range(tile_height):
            for c in range(tile_width):
                output[top + r][left + c] = tile["color"]
        shape = assignment[index]
        st, sb, sl, sr = shape["bbox"]
        pattern = [row[sl : sr + 1] for row in grid[st : sb + 1]]
        margin_r = (tile_height - len(pattern)) // 2
        margin_c = (tile_width - len(pattern[0])) // 2
        for r, row in enumerate(pattern):
            for c, value in enumerate(row):
                if value == shape["color"]:
                    output[top + margin_r + r][left + margin_c + c] = value
    return output
