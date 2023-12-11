with open('input.txt', 'r') as reader:
    data = reader.read().splitlines()

time, distance = [int(''.join(datum.split()[1:])) for datum in data]
print(time, distance)

values = [(i, (time - i) * i) for i in range(time) if (time - i) * i > distance]

print(f'res={len(values)}')
