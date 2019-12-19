def part01(wire1, wire2):
    visited1 = _visit(wire1)
    visited2 = _visit(wire2)
    crossover = _intersection(visited1, visited2)
    distances = [_manhattan(c[0], c[1], 0, 0) for c in crossover]
    return min(distances)


def part02(code, target=19690720):
    for noun in range(100):
        for verb in range(100):
            new_code = code.copy()
            new_code[1] = noun
            new_code[2] = verb
            new_code = part01(new_code)
            if new_code[0] == target:
                return 100 * noun + verb

def _visit(wire):
    visited = []
    x, y = 0, 0
    for w in wire:
        dir = w[0]
        len = int(w[1:])
        if dir == 'R':
            visited += [(x_right,y) for x_right in range(x, x+len)]
            x += len
        if dir == 'L':
            visited += [(x_left,y) for x_left in range(x, x-len, -1)]
            x -= len
        if dir == 'U':
            visited += [(x,y_up) for y_up in range(y, y+len)]
            y += len
        if dir == 'D':
            visited += [(x,y_down) for y_down in range(y, y-len, -1)]
            y -= len
    return visited[1:]

def _intersection(lst1, lst2):
    return set(lst1).intersection(lst2)

def _manhattan(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)
