# dictionary of letters to numbers
words_to_numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open(0) as file:
    inp = file.readlines()
    s = 0
    for line in inp:
        s_ptr = 0
        l_ptr = len(line) - 1

        first_digit = None
        last_digit = None

        # find a number from the left and from the right of the line
        # only get first and last digit
        f_word = ""
        l_word = ""
        while first_digit is None or last_digit is None:
            if first_digit is None:
                if line[s_ptr].isnumeric():
                    first_digit = int(line[s_ptr])
                else:
                    f_word += line[s_ptr]

                    for key in words_to_numbers.keys():
                        if key in f_word:
                            first_digit = words_to_numbers[key]
                            break
                    s_ptr += 1


            if last_digit is None:
                if line[l_ptr].isnumeric():
                    last_digit = int(line[l_ptr])
                else:
                    l_word = line[l_ptr] + l_word

                    for key in words_to_numbers.keys():
                        if key in l_word:
                            last_digit = words_to_numbers[key]
                            break
                    l_ptr -= 1

        s += (first_digit*10 + last_digit)

print(s)

