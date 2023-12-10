import re
from collections import defaultdict

with open('input.txt') as reader:
    data = reader.read().splitlines()

cards = defaultdict(lambda: 1)

res = 0
for idx, datum in enumerate(data):
    splitted = re.split('(: | \| )', datum)
    winning_numbers = set(splitted[2].strip().split())
    my_numbers = set(splitted[4].strip().split())

    matches = len(winning_numbers.intersection(my_numbers))
    for i in range(1, matches + 1):
        cards[idx + i] += cards[idx]

    res += cards[idx]

print(cards)
print(f'res={res}')