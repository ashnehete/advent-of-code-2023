import math

with open('input.txt', 'r') as reader:
    instructions, _, *data = reader.read().splitlines()

nodes = {}
for datum in data:
    nodes[datum[:3]] = {'L': datum[7:10], 'R': datum[12:15]}

START = 'A'
END = 'Z'


def get_steps(start_node: str) -> int:
    i = 0
    curr = start_node
    while not curr.endswith(END):
        direction = instructions[i % len(instructions)]
        curr = nodes[curr][direction]
        i += 1

    return i


steps = []
for node in nodes:
    if node.endswith(START):
        steps.append(get_steps(node))

print(math.lcm(*steps))
