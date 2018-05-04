import argparse
import re


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help="Option to Specify NFA file")
    parser.add_argument('-d', help="Option to Specify DFA file")
    parser.add_argument('REGEX', help="Regex file Location", type=str)
    parser.add_argument('INPUT', help="Input file Location", type=str)
    args = parser.parse_args()
    regexextract(args.REGEX, args.INPUT)


def regexextract(rfile, ifile):
    inputfile = open(rfile, "r").readline().strip()
    regex = "^" + inputfile + "$"
    print("REGEX PATTERN FOUND: "+regex)
    linematch(regex, ifile)


def linematch(pattern, file):
    inputfile = open(file, "r")
    regex = re.compile(pattern)
    print("\nMATCHES FOUND:")
    for line in inputfile:
        matches = regex.findall(line)
        for word in matches:
            print(word)


if __name__ == "__main__":
    run()
