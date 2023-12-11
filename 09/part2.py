with open('input.txt', 'r') as reader:
    data = [[int(record) for record in line.split()] for line in reader.read().splitlines()]


def get_next(sequence: list) -> list:
    return [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]


res = 0
for datum in data:
    ans = datum[0]
    curr = datum

    flag = -1
    while any(curr):
        nxt = get_next(curr)
        ans += flag * nxt[0]
        flag = -flag
        curr = nxt

    res += ans

print(f'res={res}')
