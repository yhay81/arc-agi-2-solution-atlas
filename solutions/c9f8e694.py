def _recolor_row_payload_from_leading_key(array):
    counts = {}
    for row in array:
        for value in row:
            if value:
                counts[value] = counts.get(value, 0) + 1
    values = list(counts)
    if len(values) < 3:
        return [row[:] for row in array]
    payload = max(values, key=counts.get)
    key_colors = set()
    output = [row[:] for row in array]
    changed = False
    for row_index, row in enumerate(array):
        occupied = [i for i, value in enumerate(row) if value != 0]
        if not len(occupied):
            continue
        key = int(row[int(occupied[0])])
        if key == payload:
            return [item[:] for item in array]
        key_colors.add(key)
        payload_cells = [i for i, value in enumerate(row) if value == payload]
        if payload_cells:
            for i in payload_cells:
                output[row_index][i] = key
            changed = True
    if len(key_colors) < 2 or not changed:
        return [row[:] for row in array]
    return output


def solve(grid):
    return _recolor_row_payload_from_leading_key(grid)
