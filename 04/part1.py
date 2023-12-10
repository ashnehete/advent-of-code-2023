import re

with open('input.txt') as reader:
    data = reader.read().splitlines()

res = 0
for datum in data:
    splitted = re.split('(: | \| )', datum)
    winning_numbers = set(splitted[2].strip().split())
    my_numbers = set(splitted[4].strip().split())

    matches = len(winning_numbers.intersection(my_numbers))
    if matches > 0:
        res += pow(2, matches - 1)

print(f'res={res}')
