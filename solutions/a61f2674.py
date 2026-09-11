def _keep_longest_and_shortest_vertical_runs(array):
    colors = {v for row in array for v in row if v != 0}
    if len(colors) != 1:
        return [row[:] for row in array]
    color = next(iter(colors))
    counts = [sum(row[c] == color for row in array) for c in range(len(array[0]))]
    positive_counts = [count for count in counts if count > 0]
    if len(positive_counts) < 3:
        return [row[:] for row in array]
    shortest, longest = min(positive_counts), max(positive_counts)
    shortest_cols = [c for c, count in enumerate(counts) if count == shortest]
    longest_cols = [c for c, count in enumerate(counts) if count == longest]
    if shortest == longest or len(shortest_cols) != 1 or len(longest_cols) != 1:
        return [row[:] for row in array]
    shortest_col, longest_col = shortest_cols[0], longest_cols[0]
    output = [[0] * len(array[0]) for _ in array]
    for r, row in enumerate(array):
        if row[longest_col] != 0:
            output[r][longest_col] = 1
        if row[shortest_col] != 0:
            output[r][shortest_col] = 2
    return output


def solve(grid):
    return _keep_longest_and_shortest_vertical_runs(grid)
