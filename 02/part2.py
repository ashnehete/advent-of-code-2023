with open('input.txt') as reader:
    data = reader.read().splitlines()

res = 0
for datum in data:
    game, *subsets = datum.replace(':', ';').split('; ')

    minimum = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for record in subsets:
        balls = record.split(', ')

        for ball in balls:
            number, color = ball.split()
            minimum[color] = max(minimum[color], int(number))

    power = minimum['red'] * minimum['green'] * minimum['blue']
    print(power)
    res += power

print(f'res={res}')
