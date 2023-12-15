# parse input from stdin
inp = [line.strip() for line in open(0).readlines()]

part_numbers = []

# check if ch is a symbol
def is_symbol(ch):
    # not a '.' and not a digit
    return ch != '.' and (not ch.isdigit())

def check_neighbour_symbols(inp, i, j):
    pass


for j in range(len(inp)):
    line = inp[j]
    # get numbers from the line
    # check if the numbers have a symbol adjacent to it
    has_adjacent_symbol = False
    num = ""
    for i in range(len(line)):
        if line[i].isdigit():
            num += line[i]
            if is_symbol(line[i-1]) or is_symbol(line[i+1])
                or is_symbol(inp[j-1][i] or is_symbol(inp[j+1][i])
                or is_symbol(inp[j-1][i-1]

        elif line[i] == '.':
            if num != "" and has_adjacent_symbol:
                part_numbers.append(int(num))

                num = ""
                has_adjacent_symbol = False
            else:
                num = ""
        # is a symbol
        else:





