def solve(grid):
    source = [list(row) for row in grid]
    if not source or not source[0]:
        return source
    counts = {}
    for row in source:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    background = max(counts, key=counts.get)
    objects = []
    for color in sorted(value for value in counts if value != background):
        positions = [
            (row, col)
            for row, line in enumerate(source)
            for col, value in enumerate(line)
            if value == color
        ]
        min_row = min(row for row, _ in positions)
        min_col = min(col for _, col in positions)
        cells = {(row - min_row, col - min_col) for row, col in positions}
        height = max(row for row, _ in cells) + 1
        width = max(col for _, col in cells) + 1
        raw_size = max(height, width)
        desired_size = raw_size + (raw_size % 2 == 0)
        objects.append(
            {
                "color": color,
                "cells": cells,
                "height": height,
                "width": width,
                "raw_size": raw_size,
                "desired_size": desired_size,
            }
        )
    if not objects:
        return source

    reserved = {item["desired_size"] for item in objects}
    assigned = set()
    for desired_size in sorted(reserved):
        group = sorted(
            (item for item in objects if item["desired_size"] == desired_size),
            key=lambda item: item["raw_size"],
        )
        group[0]["layer_size"] = desired_size
        assigned.add(desired_size)
        for item in group[1:]:
            layer_size = desired_size + 2
            while layer_size in reserved or layer_size in assigned:
                layer_size += 2
            item["layer_size"] = layer_size
            assigned.add(layer_size)
    canvas_size = max(assigned)

    def orbit(row, col):
        result = set()
        for _ in range(4):
            result.update(((row, col), (row, canvas_size - 1 - col)))
            row, col = col, canvas_size - 1 - row
        return result

    choices = []
    for item in objects:
        cells = item["cells"]
        height = item["height"]
        width = item["width"]
        layer_size = item["layer_size"]
        unique = {}
        for top in range(canvas_size - height + 1):
            for left in range(canvas_size - width + 1):
                completed = set()
                for row, col in cells:
                    completed.update(orbit(row + top, col + left))
                rows = [row for row, _ in completed]
                cols = [col for _, col in completed]
                dimensions = (max(rows) - min(rows) + 1, max(cols) - min(cols) + 1)
                if dimensions == (layer_size, layer_size):
                    unique[frozenset(completed)] = (len(completed) - len(cells), completed)
        if not unique:
            return source
        choices.append((item["color"], list(unique.values())))

    candidates = []

    def search(index, occupied, cost, selected):
        if index == len(choices):
            candidates.append((cost, selected.copy()))
            return
        color, options = choices[index]
        for added, completed in options:
            if not completed & occupied:
                search(
                    index + 1,
                    occupied | completed,
                    cost + added,
                    [*selected, (color, completed)],
                )

    search(0, set(), 0, [])
    if not candidates:
        return source
    best_cost = min(cost for cost, _ in candidates)
    best = [selected for cost, selected in candidates if cost == best_cost]
    if len(best) != 1:
        return source
    output = [[background] * canvas_size for _ in range(canvas_size)]
    for color, cells in best[0]:
        for row, col in cells:
            output[row][col] = color
    return output
