with open('input.txt') as reader:
    data = reader.read().splitlines()

CONSTRAINTS = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

res = 0
for datum in data:
    game, *subsets = datum.replace(':', ';').split('; ')

    try:
        for record in subsets:
            balls = record.split(', ')

            for ball in balls:
                number, color = ball.split()
                if int(number) > CONSTRAINTS[color]:
                    raise InterruptedError
    except InterruptedError:
        continue

    res += int(game[5:])

print(res)
