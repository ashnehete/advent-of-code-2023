with open('input.txt') as reader:
    data = reader.read().splitlines()

total = 0
for datum in data:
    num = 0

    # forward pass
    for char in datum:
        if char.isdigit():
            num += int(char) * 10
            break

    # backward pass
    for char in reversed(datum):
        if char.isdigit():
            num += int(char)
            break

    total += num
    print(datum, num)

print(total)
