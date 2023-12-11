import math
from collections import defaultdict

with open('sample.txt', 'r') as reader:
    data = reader.read().splitlines()

seeds = [int(seed) for seed in data[0].split()[1:]]

graph = defaultdict(lambda: {})
current_map = None
i = 1

while i < len(data):
    if data[i] == '':
        current_map = data[i + 1][:-5]
        i += 1
    else:
        dest, src, length = [int(value) for value in data[i].split()]
        graph[current_map][range(src, src + length)] = range(dest, dest + length)
    i += 1

links = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature',
         'temperature-to-humidity', 'humidity-to-location']

lowest = math.inf
for seed in seeds:
    curr = seed
    for link in links:
        for src_range, dest_range in graph[link].items():
            if curr in src_range:
                curr = dest_range.start + (curr - src_range.start)
                break

    print(f'seed={seed} loc={curr}')
    lowest = min(lowest, curr)

print(f'lowest={lowest}')
