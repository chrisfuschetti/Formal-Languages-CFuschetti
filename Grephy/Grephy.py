# Imports for libraries and support files
# This is the main file that controls the flow of the program
import argparse
import re
from alphabet import define_alphabet
from postfix import postfix_conversion
from nfa import *
from dfa import *
from evaluate import evaluate_dfa

# main run function that grabs the user input and pipes them through the other files


def run():
    n = "nfa"
    d = "dfa"
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help="Option to Specify NFA file")
    parser.add_argument('-d', help="Option to Specify DFA file")
    parser.add_argument('REGEX', help="Regex file Location", type=str)
    parser.add_argument('INPUT', help="Input file Location", type=str)
    args = parser.parse_args()
    alphabet = define_alphabet(args.INPUT)
    postfixconvert = postfix_conversion(args.REGEX, alphabet)
    nfaconvert = nfa_conversion(postfixconvert)
    dfaconvert = dfa_conversion(nfaconvert, alphabet)
    evaluate_dfa(dfaconvert, args.INPUT)
    linematch(args.REGEX, args.INPUT)
    if args.n:
        n = args.n
    if args.d:
        d = args.d
    convert_dot_graphviz_dfa(dfaconvert, d)
    convert_dot_graphviz_nfa(nfaconvert, n)

# linematch uses the re python regex to see what it would pick
# this gives us an idea pf how well the dfa is working


def linematch(pattern, file):
    inputfile = open(file, "r")
    pattern = "^" + pattern + "$"
    regex = re.compile(pattern)
    print("\nMATCHES FOUND FROM BUILT IN PYTHON REGEX:")
    for line in inputfile:
        matches = regex.findall(line)
        for word in matches:
            print(word)


# on load of the python file this will trigger and set off the run function

if __name__ == "__main__":
    run()
