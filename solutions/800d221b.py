from collections import Counter


def solve(grid):
    h, w = len(grid), len(grid[0])

    def components(cells):
        remaining = set(cells)
        found = []
        while remaining:
            seed = min(remaining)
            remaining.remove(seed)
            stack = [seed]
            component = [seed]
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (nr, nc) in remaining:
                        remaining.remove((nr, nc))
                        stack.append((nr, nc))
                        component.append((nr, nc))
            found.append(component)
        return found

    counts = Counter(value for row in grid for value in row)
    background = counts.most_common(1)[0][0]
    candidates = []
    for color in {value for row in grid for value in row if value != background}:
        centers = [
            (r, c)
            for r in range(1, h - 1)
            for c in range(1, w - 1)
            if all(grid[r + dr][c + dc] == color for dr in (-1, 0, 1) for dc in (-1, 0, 1))
        ]
        if len(centers) == 1:
            candidates.append((color, centers[0]))
    if not (len(candidates) == 1):
        raise ValueError("task assumptions are not satisfied")
    wire, (center_r, center_c) = candidates[0]
    ring = {
        (r, c) for r in range(center_r - 1, center_r + 2) for c in range(center_c - 1, center_c + 2)
    }
    branches = {
        (r, c) for r in range(h) for c in range(w) if grid[r][c] == wire and (r, c) not in ring
    }
    content = {(r, c) for r in range(h) for c in range(w) if grid[r][c] not in (background, wire)}
    blocks = components(content)
    output = [row[:] for row in grid]
    votes = []
    for branch in components(branches):
        touch = set(branch)
        for r, c in branch:
            touch.update(
                (nr, nc)
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
                if 0 <= nr < h and 0 <= nc < w
            )
        colors = [
            grid[r][c] for block in blocks if any(cell in touch for cell in block) for r, c in block
        ]
        if not (colors):
            raise ValueError("task assumptions are not satisfied")
        label = Counter(colors).most_common(1)[0][0]
        for r, c in branch:
            output[r][c] = label
        votes.extend(
            [label]
            * sum(
                any(
                    (nr, nc) in ring
                    for nr, nc in ((r, c), (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1))
                )
                for r, c in branch
            )
        )
    if not (votes):
        raise ValueError("task assumptions are not satisfied")
    output[center_r][center_c] = Counter(votes).most_common(1)[0][0]
    return output
