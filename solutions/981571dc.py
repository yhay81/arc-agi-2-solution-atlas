def solve(grid):
    if not grid or len(grid) != len(grid[0]):
        return [row[:] for row in grid]
    size = len(grid)

    def complete_once(value):
        result = [row[:] for row in value]
        for row_index in range(size):
            row = result[row_index]
            visible = [col for col, item in enumerate(row) if item != 0]
            if len(visible) == size:
                continue
            candidates = []
            for candidate_index in range(size):
                if candidate_index == row_index:
                    continue
                candidate = result[candidate_index]
                if all(candidate[col] == row[col] for col in visible):
                    candidates.append((candidate.count(0), 0, candidate_index, candidate[:]))
            for candidate_index in range(size):
                candidate = [result[row][candidate_index] for row in range(size)]
                if all(candidate[col] == row[col] for col in visible):
                    candidates.append((candidate.count(0), 1, candidate_index, candidate))
            if candidates:
                candidate = min(candidates, key=lambda item: item[:3])[3]
                for col in range(size):
                    if row[col] == 0:
                        result[row_index][col] = candidate[col]
        return result

    result = complete_once(grid)
    while True:
        next_result = complete_once(result)
        transposed = complete_once([list(row) for row in zip(*result)])
        transposed = [list(row) for row in zip(*transposed)]
        if next_result == result and transposed == result:
            break
        result = transposed
    for row in range(size):
        for col in range(row + 1, size):
            if result[row][col] == 0 and result[col][row] != 0:
                result[row][col] = result[col][row]
            elif result[col][row] == 0 and result[row][col] != 0:
                result[col][row] = result[row][col]
    return result
