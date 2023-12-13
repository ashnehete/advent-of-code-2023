from dataclasses import dataclass


@dataclass
class Cell:
    x: int
    y: int

    def __add__(self, other):
        return Cell(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash((self.x, self.y))


Table = dict[Cell, str]

NEIGHBOURS = [
    Cell(1, 0), Cell(-1, 0), Cell(0, 1), Cell(0, -1)
]

PIPES = {
    "|": (Cell(1, 0), Cell(-1, 0)),
    "-": (Cell(0, 1), Cell(0, -1)),
    "L": (Cell(-1, 0), Cell(0, 1)),
    "J": (Cell(-1, 0), Cell(0, -1)),
    "7": (Cell(0, -1), Cell(1, 0)),
    "F": (Cell(0, 1), Cell(1, 0)),
}


def parse_table(raw: list[str]) -> Table:
    table = {}

    for row, line in enumerate(raw):
        for col, cell in enumerate(line):
            table[Cell(row, col)] = cell

    return table


def get_start(table: Table):
    for k, v in table.items():
        if v == 'S':
            return k


def moves(curr: Cell, cell_str: str):
    return [curr + o for o in PIPES[cell_str]]


def find_start_neighbours(table: Table, start: Cell):
    for neighbour in NEIGHBOURS:
        nxt = start + neighbour
        if nxt in table and table[nxt] != '.' and start in moves(nxt, table[nxt]):
            return nxt


def main(raw: list[str]):
    table = parse_table(raw)
    loop = get_loop(table)
    area = get_area(loop)
    return get_interior_points(area, len(loop) - 1)


def get_loop(table: Table):
    start = get_start(table)
    curr = find_start_neighbours(table, start)

    points = [start]
    while True:
        last = points[-1]
        points.append(curr)
        a, b = moves(curr, table[curr])

        if (a == start or b == start) and last != start:
            break

        curr = a if b == last else b

    points.append(start)
    return points


def get_area(points: list[Cell]):
    """
    Shoelace formula for area of algorithm
    """
    area = 0
    for a, b in zip(points, points[1:]):
        area += (a.x * b.y) - (b.x * a.y)

    return area / 2


def get_interior_points(area, points):
    """
    Pick's theorem
    """
    return int(abs(area) - 0.5 * points + 1)


if __name__ == '__main__':
    with open('input.txt') as reader:
        data = reader.read().splitlines()

    res = main(data)
    print(res)
