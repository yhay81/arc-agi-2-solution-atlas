def solve(grid):
    array = [[int(value) for value in row] for row in grid]
    height = len(array)
    width = len(array[0]) if height else 0
    colors = sorted({value for row in array for value in row})
    counts = {}
    for color in colors:
        prefix = [[0] * (width + 1) for _ in range(height + 1)]
        for row in range(height):
            running = 0
            for col in range(width):
                running += array[row][col] == color
                prefix[row + 1][col + 1] = prefix[row][col + 1] + running
        counts[color] = prefix

    def count(color, top, left, bottom, right):
        prefix = counts[color]
        return (
            prefix[bottom + 1][right + 1]
            - prefix[top][right + 1]
            - prefix[bottom + 1][left]
            + prefix[top][left]
        )

    best = None
    for color_index, first in enumerate(colors):
        for second in colors[color_index + 1 :]:
            allowed = [[value in (first, second) for value in row] for row in array]
            heights = [0] * width
            rectangle = None
            for row in range(height):
                for col in range(width):
                    heights[col] = heights[col] + 1 if allowed[row][col] else 0
                stack = []
                for col in range(width + 1):
                    current = heights[col] if col < width else 0
                    while stack and heights[stack[-1]] > current:
                        index = stack.pop()
                        rectangle_height = heights[index]
                        left = stack[-1] + 1 if stack else 0
                        right = col - 1
                        top = row - rectangle_height + 1
                        if rectangle_height < 2 or right - left + 1 < 2:
                            continue
                        first_count = count(first, top, left, row, right)
                        second_count = count(second, top, left, row, right)
                        if not min(first_count, second_count) or first_count == second_count:
                            continue
                        base, marker = (
                            (first, second) if first_count > second_count else (second, first)
                        )
                        candidate = (
                            rectangle_height * (right - left + 1),
                            max(first_count, second_count),
                            -top,
                            -left,
                            top,
                            left,
                            row,
                            right,
                        )
                        if rectangle is None or candidate > rectangle[0]:
                            rectangle = candidate, base, marker
                    stack.append(col)
            if rectangle is None:
                continue
            score, base, marker = rectangle
            top, left, bottom, right = score[-4:]
            output = [row[left : right + 1] for row in array[top : bottom + 1]]
            marker_rows = {
                row
                for row in range(len(output))
                for col in range(len(output[0]))
                if output[row][col] == marker
            }
            marker_cols = {
                col
                for row in range(len(output))
                for col in range(len(output[0]))
                if output[row][col] == marker
            }
            for row in marker_rows:
                output[row] = [marker] * len(output[row])
            for col in marker_cols:
                for row in range(len(output)):
                    output[row][col] = marker
            candidate = len(output) * len(output[0]), score[1], output
            if best is None or candidate[:2] > best[:2]:
                best = candidate
    if best is None:
        raise ValueError("no dominant two-color rectangle")
    return best[2]
