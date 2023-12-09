from collections import defaultdict

with open('input.txt') as reader:
    data = [list(line) for line in reader.read().splitlines()]

columns = len(data)
rows = len(data[0])

DIRECTIONS = [
    [-1, -1],
    [-1, 0],
    [-1, 1],

    [0, -1],
    [0, 0],
    [0, 1],

    [1, -1],
    [1, 0],
    [1, 1],
]

GEAR = '*'
parts = defaultdict(list)


def gear_location(i, j):
    for dx, dy in DIRECTIONS:
        if 0 <= i + dx < rows and 0 <= j + dy < columns and data[i + dx][j + dy] == GEAR:
            return i + dx, j + dy

    return None


part_number = 0
part_gear = None

for i in range(columns):
    for j in range(rows):
        cell = data[i][j]

        if cell.isdigit():
            part_number = part_number * 10 + int(cell)
            if not part_gear:
                part_gear = gear_location(i, j)

        else:
            if part_gear:
                parts[part_gear].append(part_number)

            part_gear = None
            part_number = 0

    if part_gear:
        parts[part_gear].append(part_number)

    part_gear = None
    part_number = 0

res = 0
for gear in parts:
    if len(parts[gear]) == 2:
        res += parts[gear][0] * parts[gear][1]

print(f'res={res}')