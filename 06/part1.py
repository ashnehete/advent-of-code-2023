with open('input.txt', 'r') as reader:
    data = reader.read().splitlines()

time, distance = [datum.split()[1:] for datum in data]
input = {int(k): int(v) for k, v in zip(time, distance)}

res = 1
for t, d in input.items():
    values = [(i, (t - i) * i) for i in range(t) if (t - i) * i > d]
    res *= len(values)

print(f'res={res}')
