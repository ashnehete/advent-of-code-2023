from collections import defaultdict

with open('input.txt', 'r') as reader:
    data = reader.read().splitlines()

seeds = data[0].split()[1:]
seeds_range = []
i = 0
while i < len(seeds):
    start, length = int(seeds[i]), int(seeds[i + 1])
    seeds_range.append(range(start, start + length))
    i += 2
print(seeds_range)

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

location = 0
while True:
    curr = location
    for link in reversed(links):
        for src_range, dest_range in graph[link].items():
            if curr in dest_range:
                curr = src_range.start + (curr - dest_range.start)
                break

    for seed_range in seeds_range:
        if curr in seed_range:
            print(f'location={location}')
            exit()

    location += 1
