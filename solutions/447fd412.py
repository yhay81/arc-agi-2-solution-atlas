def _components(grid, color):
    height, width = len(grid), len(grid[0])
    unseen = {
        (row, col) for row in range(height) for col in range(width) if grid[row][col] == color
    }
    result = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        stack = [start]
        component = []
        while stack:
            row, col = stack.pop()
            component.append((row, col))
            for neighbor in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    stack.append(neighbor)
        result.append(component)
    return result


def _bounds(cells):
    rows, cols = zip(*cells)
    return min(rows), min(cols), max(rows), max(cols)


def _shape(cells):
    top, left, bottom, right = _bounds(cells)
    return {(row - top, col - left) for row, col in cells}, bottom - top + 1, right - left + 1


def _scaled(shape, scale):
    return {
        (row * scale + dr, col * scale + dc)
        for row, col in shape
        for dr in range(scale)
        for dc in range(scale)
    }


def _copy_scaled(grid, output, box, origin, scale):
    top, left, bottom, right = box
    height, width = len(output), len(output[0])
    for row in range(bottom - top + 1):
        for col in range(right - left + 1):
            value = grid[top + row][left + col]
            if value:
                for dr in range(scale):
                    for dc in range(scale):
                        target = origin[0] + row * scale + dr, origin[1] + col * scale + dc
                        if 0 <= target[0] < height and 0 <= target[1] < width:
                            output[target[0]][target[1]] = value


def solve(grid):
    colors = sorted({value for row in grid for value in row if value})
    if len(colors) != 2:
        return [row[:] for row in grid]
    output = [row[:] for row in grid]
    for object_color, marker_color in ((colors[0], colors[1]), (colors[1], colors[0])):
        objects = _components(grid, object_color)
        markers = _components(grid, marker_color)
        if not objects or not markers:
            continue
        template = max(objects, key=len)
        template_set = set(template)
        prototype = [
            marker
            for marker in markers
            if any(
                (row + dr, col + dc) in template_set
                for row, col in marker
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
            )
        ]
        if not prototype or len(prototype) >= len(markers):
            continue

        template_box = _bounds(template + [cell for marker in prototype for cell in marker])
        template_top, template_left, _, _ = template_box
        prototype_info = [_shape(marker) for marker in prototype]
        prototype_boxes = [_bounds(marker) for marker in prototype]
        targets = [marker for marker in markers if marker not in prototype]
        scales = {
            target_height // proto_height
            for target in targets
            for _, target_height, target_width in [_shape(target)]
            for _, proto_height, proto_width in prototype_info
            if target_height % proto_height == target_width % proto_width == 0
            and target_height // proto_height == target_width // proto_width
        }
        for anchor in targets:
            anchor_top, anchor_left, _, _ = _bounds(anchor)
            anchor_shape, anchor_height, anchor_width = _shape(anchor)
            for scale in sorted(scales):
                proto_shape, proto_height, proto_width = prototype_info[0]
                if (
                    anchor_shape != _scaled(proto_shape, scale)
                    or anchor_height != proto_height * scale
                    or anchor_width != proto_width * scale
                ):
                    continue
                proto_top, proto_left, _, _ = prototype_boxes[0]
                origin = (
                    anchor_top - (proto_top - template_top) * scale,
                    anchor_left - (proto_left - template_left) * scale,
                )
                expected = [
                    (
                        origin[0] + (box[0] - template_top) * scale,
                        origin[1] + (box[1] - template_left) * scale,
                        height * scale,
                        width * scale,
                        _scaled(shape, scale),
                    )
                    for (shape, height, width), box in zip(prototype_info, prototype_boxes)
                ]
                target_info = [
                    (*_bounds(target)[:2], *_shape(target)[1:], _shape(target)[0])
                    for target in targets
                ]
                if all(item in target_info for item in expected):
                    _copy_scaled(grid, output, template_box, origin, scale)
                    break
    return output
