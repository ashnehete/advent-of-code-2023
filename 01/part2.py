with open('input.txt') as reader:
    data = reader.read().splitlines()

total = 0
digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def starts_with_digit(string: str):
    for i, digit in enumerate(digits):
        if string.startswith(digit):
            return i + 1

    return False


for datum in data:
    numbers = []

    for i, char in enumerate(datum):
        if char.isdigit():
            numbers.append(int(char))
        elif d := starts_with_digit(datum[i:]):
            numbers.append(d)

    print(datum, numbers)
    total += numbers[0] * 10 + numbers[-1]

print(total)
