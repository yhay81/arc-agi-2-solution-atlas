def solve(grid):
    separators = [col for col in range(len(grid[0])) if all(row[col] == 0 for row in grid)]
    edges = [-1, *separators, len(grid[0])]
    panels = [
        [row[left + 1 : right] for row in grid]
        for left, right in zip(edges, edges[1:])
        if right > left + 1
    ]

    output = []
    for panel in panels:
        zeros = [
            (row, col)
            for row, line in enumerate(panel)
            for col, cell in enumerate(line)
            if cell == 0
        ]
        if not zeros:
            color = 2
        elif any(col in (0, len(panel[0]) - 1) for _, col in zeros):
            color = 3
        elif any(row == len(panel) - 1 for row, _ in zeros):
            color = 4
        else:
            color = 8
        output.append([color] * 3)
    return output
