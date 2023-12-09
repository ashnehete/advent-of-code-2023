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

SYMBOLS = {'$', '%', '*', '+', '@', '=', '/', '-', '&', '#'}


def is_part_counted(i, j):
    for dx, dy in DIRECTIONS:
        if 0 <= i + dx < rows and 0 <= j + dy < columns and data[i + dx][j + dy] in SYMBOLS:
            return True

    return False


res = 0

part_number = 0
part_flag = False

for i in range(columns):
    for j in range(rows):
        cell = data[i][j]

        if cell.isdigit():
            part_number = part_number * 10 + int(cell)
            part_flag = part_flag | is_part_counted(i, j)

        else:
            if part_flag:
                res += part_number

            part_flag = False
            part_number = 0

    if part_flag:
        res += part_number

    part_flag = False
    part_number = 0

print(f'res={res}')
