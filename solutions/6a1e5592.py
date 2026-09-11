def solve(grid):
    height, width = len(grid), len(grid[0]) if grid else 0
    source = [row[:] for row in grid]
    if height < 2 or not width:
        return source
    background = source[0][0]
    upper_bottom = max((row for row in range(height) if background in source[row]), default=-1)
    if upper_bottom < 0:
        return source
    upper = {(row, col) for row in range(upper_bottom + 1) for col in range(width)}
    lower = {(row, col) for row in range(upper_bottom + 1, height) for col in range(width)}
    upper_colors = {source[row][col] for row, col in upper if source[row][col] != background}
    lower_colors = {
        source[row][col]
        for row, col in lower
        if source[row][col] not in (background, *upper_colors)
    }
    if len(upper_colors) != 1 or len(lower_colors) != 1:
        return source
    fragment_color, exemplar_color = next(iter(upper_colors)), next(iter(lower_colors))

    def components(cells):
        result, seen = [], set()
        for start in sorted(cells):
            if start in seen:
                continue
            seen.add(start)
            stack, component = [start], []
            while stack:
                row, col = stack.pop()
                component.append((row, col))
                for neighbor in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                    if neighbor in cells and neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            result.append(component)
        return result

    fragments = components({cell for cell in upper if source[cell[0]][cell[1]] == fragment_color})
    exemplars = components({cell for cell in lower if source[cell[0]][cell[1]] == exemplar_color})
    if not fragments or len(fragments) != len(exemplars):
        return source

    def shape(component):
        top = min(row for row, _ in component)
        left = min(col for _, col in component)
        return {(row - top, col - left) for row, col in component}, top, left

    fragment_data = [shape(component) for component in fragments]
    exemplar_data = []
    for component in exemplars:
        mask, top, left = shape(component)
        exemplar_data.append((mask, top + upper_bottom + 1, left))
    candidates, origins = [], {}
    for fragment_index, (fragment, fragment_top, fragment_left) in enumerate(fragment_data):
        matches = []
        fragment_height = max(row for row, _ in fragment) + 1
        fragment_width = max(col for _, col in fragment) + 1
        for exemplar_index, (exemplar, exemplar_top, exemplar_left) in enumerate(exemplar_data):
            prefix = {(row, col) for row, col in exemplar if row < fragment_height}
            if not prefix:
                continue
            top = min(row for row, _ in prefix)
            left = min(col for _, col in prefix)
            bottom = max(row for row, _ in prefix)
            right = max(col for _, col in prefix)
            cropped = {(row - top, col - left) for row, col in prefix}
            if (bottom - top + 1, right - left + 1) != (
                fragment_height,
                fragment_width,
            ) or cropped != fragment:
                continue
            matches.append(exemplar_index)
            origins[fragment_index, exemplar_index] = (exemplar_top + top, exemplar_left + left)
        candidates.append(matches)
    if any(not matches for matches in candidates):
        return source
    assignments = []

    def search(index, used, chosen):
        if len(assignments) > 1:
            return
        if index == len(candidates):
            assignments.append(chosen[:])
            return
        for exemplar_index in candidates[index]:
            if exemplar_index not in used:
                search(index + 1, used | {exemplar_index}, chosen + [exemplar_index])

    search(0, set(), [])
    if len(assignments) != 1:
        return source
    output = [[background if value == background else 0 for value in row] for row in source]
    for fragment_index, exemplar_index in enumerate(assignments[0]):
        fragment, fragment_top, fragment_left = fragment_data[fragment_index]
        exemplar, exemplar_top, exemplar_left = exemplar_data[exemplar_index]
        prefix_top, prefix_left = origins[fragment_index, exemplar_index]
        shift_row, shift_col = fragment_top - prefix_top, fragment_left - prefix_left
        for row, col in exemplar:
            target_row, target_col = exemplar_top + row + shift_row, exemplar_left + col + shift_col
            if 0 <= target_row < height and 0 <= target_col < width:
                output[target_row][target_col] = 1
    return output
