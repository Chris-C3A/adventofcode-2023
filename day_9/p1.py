# parse input
inp = open(0).readlines()

inp = list(map(lambda x: x.strip(), inp))

total = 0

for sequence in inp:
    curr_seq = list(map(int, sequence.split(' ')))
    sequences = [curr_seq]
    # keep finding the sequence of differences until the sequence is all zeros
    while not all([n == 0 for n in curr_seq]):
        next_seq = []
        for i in range(1, len(curr_seq)):
            next_seq.append(int(curr_seq[i] - curr_seq[i-1]))
        curr_seq = next_seq
        sequences.append(curr_seq)

    # get next number in sequence
    next_num = sum(sequence[-1] for sequence in sequences)

    total += next_num

print(total)



