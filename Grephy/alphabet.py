# This file extracts the input file and finds the alphabet inside it
# the set type makes it easy to only get unique  characters


def define_alphabet(inputfile):
    alphabet = set()
    file = open(inputfile, "r")
    for line in file:
        for char in line:
            if char != '\n':
                alphabet.add(char)
    file.close()
    print("Alphabet Found:")
    print(*alphabet)
    return alphabet
