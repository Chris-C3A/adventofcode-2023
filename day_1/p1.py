

with open('inp.txt') as file:
    inp = file.readlines()
    s = 0
    for line in inp:
        s_ptr = 0
        l_ptr = len(line) - 1

        # find a number from the left and from the right of the line
        # only get first and last digit
        while not (line[s_ptr].isnumeric() and line[l_ptr].isnumeric()):
            if not line[s_ptr].isnumeric():
                s_ptr += 1

            if not line[l_ptr].isnumeric():
                l_ptr -= 1

        s += int(line[s_ptr])*10 + int(line[l_ptr])

print(s)

