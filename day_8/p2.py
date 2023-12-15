inp = open(0).readlines()

inp = list(map(lambda x: x.strip(), inp))

instructions = inp[0]

network = {}

# ignore inp[1] blank line

# find all nodes that end with A and simultaneously navigate them
# until all these nodes end with a node that ends with Z

# parse network
for line in inp[2:]:
    node, destinations = line.split(' = ')

    L, R = destinations.replace('(', '').replace(')', '').split(', ')
    network[node] = {"L": L, "R": R}

# get start nodes which ends with A
start_nodes = list(filter(lambda node: node.endswith('A'), network.keys()))

print(start_nodes)

current_nodes = start_nodes
steps = 0
while not all(node.endswith('Z') for node in current_nodes):
    for i in range(len(current_nodes)):
        current_nodes[i] = network[current_nodes[i]][instructions[0]]
    steps += 1
    instructions = instructions[1:] + instructions[0]

print(steps)

