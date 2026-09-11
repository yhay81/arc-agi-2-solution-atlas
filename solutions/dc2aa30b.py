def _sort_three_by_three_tiles_by_count(array):
    height, width = len(array), len(array[0])
    if height != width:
        return [r[:] for r in array]

    layouts = []
    for tile_size in range(1, height):
        if (height + 1) % (tile_size + 1):
            continue
        side = (height + 1) // (tile_size + 1)
        separators = [tile_size + index * (tile_size + 1) for index in range(side - 1)]
        if side > 1 and all(
            all(value == 0 for value in array[index])
            and all(array[row][index] == 0 for row in range(height))
            for index in separators
        ):
            layouts.append((tile_size, side))
    if not layouts:
        return [r[:] for r in array]
    tile_height, side = max(layouts)
    tile_width = tile_height
    starts = [index * (tile_height + 1) for index in range(side)]
    row_spans = [(start, start + tile_height) for start in starts]
    col_spans = [(start, start + tile_width) for start in starts]

    blocks = []
    for top, bottom in row_spans:
        for left, right in col_spans:
            tile = [row[left:right] for row in array[top:bottom]]
            blocks.append((sum(v == 1 for r in tile for v in r), tile))
    counts = [count for count, _ in blocks]
    if len(set(counts)) != len(blocks):
        return [r[:] for r in array]
    ascending = [tile for _, tile in sorted(blocks, key=lambda item: item[0])]
    rows = [ascending[start : start + side] for start in range(0, len(ascending), side)]
    ordered = [tile for row in reversed(rows) for tile in row]
    output = [r[:] for r in array]
    destinations = [(top, left) for top, _ in row_spans for left, _ in col_spans]
    for tile, (top, left) in zip(ordered, destinations):
        for offset, row in enumerate(tile):
            output[top + offset][left : left + tile_width] = row
    return output


def solve(grid):
    return _sort_three_by_three_tiles_by_count([r[:] for r in grid])
