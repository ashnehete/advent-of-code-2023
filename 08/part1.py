with open('input.txt', 'r') as reader:
    instructions, _, *data = reader.read().splitlines()

nodes = {}
for datum in data:
    nodes[datum[:3]] = {'L': datum[7:10], 'R': datum[12:15]}

START = 'AAA'
END = 'ZZZ'

i = 0
curr = START
while curr != END:
    direction = instructions[i % len(instructions)]
    curr = nodes[curr][direction]
    i += 1

print(i)
