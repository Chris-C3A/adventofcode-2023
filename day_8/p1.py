inp = open(0).readlines()

inp = list(map(lambda x: x.strip(), inp))

instructions = inp[0]

network = {}

# ignore inp[1] blank line

# parse network
for line in inp[2:]:
    node, destinations = line.split(' = ')

    L, R = destinations.replace('(', '').replace(')', '').split(', ')
    network[node] = {"L": L, "R": R}

current = "AAA"
steps = 0
while current != "ZZZ":
    for instruction in instructions:
        current = network[current][instruction]
        steps += 1

print(steps)

