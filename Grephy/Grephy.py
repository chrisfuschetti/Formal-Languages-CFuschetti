import argparse
import re
from alphabet import define_alphabet
from postfix import postfix_conversion
from nfa import nfa_conversion
from dfa import dfa_conversion
from evaluate import evaluate_dfa


def run():
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


def linematch(pattern, file):
    inputfile = open(file, "r")
    regex = re.compile(pattern)
    print("\nMATCHES FOUND FROM BUILT IN PYTHON REGEX:")
    for line in inputfile:
        matches = regex.findall(line)
        for word in matches:
            print(word)


if __name__ == "__main__":
    run()
