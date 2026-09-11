from collections import Counter


def solve(grid):
    def modes(lines):
        labels = []
        score = 0
        for line in lines:
            n = Counter(line)
            value, count = n.most_common(1)[0]
            labels.append(value)
            score += count / len(line)
        return labels, score / len(lines)

    def runs(labels):
        out = []
        for v in labels:
            if not out or out[-1] != v:
                out.append(v)
        return out

    rows, rs = modes(grid)
    cols, cs = modes(list(zip(*grid)))
    rr, cr = runs(rows), runs(cols)
    rv = len(rr) < len(rows) and len(rr) >= 2
    cv = len(cr) < len(cols) and len(cr) >= 2
    if rv and (not cv or rs >= cs):
        return [[v] for v in rr]
    if cv:
        return [cr]
    return [r[:] for r in grid]
