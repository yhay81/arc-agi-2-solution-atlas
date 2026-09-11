from collections import Counter, defaultdict, deque
from typing import Any

type Component = dict[str, Any]


def _components(grid, background: int) -> list[Component]:
    height, width = len(grid), len(grid[0])
    visited: set[tuple[int, int]] = set()
    result = []
    for row in range(height):
        for col in range(width):
            if grid[row][col] == background or (row, col) in visited:
                continue
            queue = deque([(row, col)])
            visited.add((row, col))
            cells = []
            color_positions: dict[int, list[tuple[int, int]]] = defaultdict(list)
            while queue:
                current_row, current_col = queue.popleft()
                cells.append((current_row, current_col))
                color_positions[grid[current_row][current_col]].append((current_row, current_col))
                for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    neighbor = current_row + dr, current_col + dc
                    if (
                        0 <= neighbor[0] < height
                        and 0 <= neighbor[1] < width
                        and neighbor not in visited
                        and grid[neighbor[0]][neighbor[1]] != background
                    ):
                        visited.add(neighbor)
                        queue.append(neighbor)
            rows = [r for r, _ in cells]
            cols = [c for _, c in cells]
            result.append(
                {
                    "cells": cells,
                    "color_positions": color_positions,
                    "bbox": (min(rows), max(rows), min(cols), max(cols)),
                }
            )
    return result


def _choose_anchor(anchors: list[tuple[int, int]], height: int, width: int) -> tuple[int, int]:
    def score(point: tuple[int, int]) -> tuple[int, int, int, int, int]:
        row, col = point
        row_margin = min(row, height - 1 - row)
        col_margin = min(col, width - 1 - col)
        return row_margin + col_margin, row_margin, col_margin, -row, -col

    return max(anchors, key=score)


def _targets(
    grid, components: list[Component]
) -> tuple[dict[int, tuple[str, int]], dict[int, tuple[int, int]]]:
    height, width = len(grid), len(grid[0])
    singleton_positions: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for component in components:
        if len(component["cells"]) == 1:
            row, col = component["cells"][0]
            singleton_positions[grid[row][col]].append((row, col))

    targets: dict[int, tuple[str, int]] = {}
    anchors: dict[int, tuple[int, int]] = {}
    for color, positions in singleton_positions.items():
        markers = [
            locations[0]
            for component in components
            if len(component["cells"]) > 1
            and len(locations := component["color_positions"].get(color, ())) == 1
        ]
        if not markers:
            side = [(row, col) for row, col in positions if col in (0, width - 1)]
            ends = [(row, col) for row, col in positions if row in (0, height - 1)]
            if len(side) >= 2 and len({row for row, _ in side}) == 1:
                targets[color] = "row", side[0][0]
                anchors[color] = side[0]
            elif len(ends) >= 2 and len({col for _, col in ends}) == 1:
                targets[color] = "col", ends[0][1]
                anchors[color] = ends[0]
            continue

        border = [
            point
            for point in positions
            if point[0] in (0, height - 1) or point[1] in (0, width - 1)
        ]
        anchor = _choose_anchor(border or positions, height, width)
        anchors[color] = anchor
        if anchor[1] in (0, width - 1):
            axis = "row"
        elif anchor[0] in (0, height - 1):
            axis = "col"
        else:
            row_cost = sum(abs(anchor[0] - row) for row, _ in markers)
            col_cost = sum(abs(anchor[1] - col) for _, col in markers)
            axis = "row" if row_cost <= col_cost else "col"
        targets[color] = axis, anchor[1] if axis == "col" else anchor[0]
    return targets, anchors


def _component_shift(component: Component, targets: dict[int, tuple[str, int]]) -> tuple[int, int]:
    constraints = []
    for color, positions in component["color_positions"].items():
        if color not in targets or len(positions) != 1:
            continue
        axis, target = targets[color]
        row, col = positions[0]
        constraints.append((target - row, 0) if axis == "row" else (0, target - col))
    return constraints[0] if len(constraints) == 1 else (0, 0)


def _compact_rows(
    components: list[Component],
    shifts: list[tuple[int, int]],
    targets: dict[int, tuple[str, int]],
    width: int,
) -> None:
    for color, (axis, target) in targets.items():
        if axis != "row":
            continue
        moving_heights = [
            component["bbox"][1] - component["bbox"][0] + 1
            for component in components
            if len(component["cells"]) > 1 and len(component["color_positions"].get(color, ())) == 1
        ]
        if moving_heights and target < max(moving_heights):
            continue

        entries = []
        for index, component in enumerate(components):
            positions = component["color_positions"].get(color, ())
            if len(component["cells"]) == 1 or len({row for row, _ in positions}) != 1:
                continue
            _, _, min_col, max_col = component["bbox"]
            dr, dc = shifts[index]
            entries.append(
                {
                    "index": index,
                    "row": positions[0][0],
                    "dr": dr,
                    "min_col": min_col,
                    "width": max_col - min_col + 1,
                    "left": min_col + dc,
                    "right": max_col + dc,
                    "column_constrained": any(
                        other_color != color and targets.get(other_color, (None,))[0] == "col"
                        for other_color in component["color_positions"]
                    ),
                }
            )
        entries.sort(key=lambda entry: entry["left"])
        last_right: int | None = None
        for entry in entries:
            expected_dr = target - entry["row"]
            if entry["column_constrained"] or expected_dr != entry["dr"] or expected_dr <= 0:
                last_right = entry["right"]
                continue
            if last_right is None:
                last_right = entry["right"]
                continue
            target_left = min(max(last_right + 2, 0), width - entry["width"])
            new_left = min(target_left, entry["left"])
            shifts[entry["index"]] = entry["dr"], new_left - entry["min_col"]
            last_right = new_left + entry["width"] - 1


def solve(grid):
    background = Counter(cell for row in grid for cell in row).most_common(1)[0][0]
    components = _components(grid, background)
    targets, _ = _targets(grid, components)
    shifts = [_component_shift(component, targets) for component in components]
    _compact_rows(components, shifts, targets, len(grid[0]))

    height, width = len(grid), len(grid[0])
    output = [[background for _ in range(width)] for _ in range(height)]
    for component, (dr, dc) in zip(components, shifts):
        for row, col in component["cells"]:
            moved = row + dr, col + dc
            if 0 <= moved[0] < height and 0 <= moved[1] < width:
                output[moved[0]][moved[1]] = grid[row][col]
    return output
