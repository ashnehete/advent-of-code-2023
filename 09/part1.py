with open('sample.txt', 'r') as reader:
    data = [[int(record) for record in line.split()] for line in reader.read().splitlines()]


def get_next(sequence: list) -> list:
    return [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]


res = 0
for datum in data:
    res += datum[-1]
    curr = datum
    while any(curr):
        nxt = get_next(curr)
        res += nxt[-1]
        curr = nxt

print(f'res={res}')
