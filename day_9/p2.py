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


    prev_num = 0
    for seq in reversed(sequences):
        prev_num = -prev_num + seq[0]


    # get next number in sequence
    # prev_num = sequences[0][0] - sum(sequence[0] for sequence in sequences[1:])

    total += prev_num

print(total)



