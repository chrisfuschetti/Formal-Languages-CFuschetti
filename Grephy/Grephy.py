import argparse
import re


def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', help="Option to Specify NFA file")
    parser.add_argument('-d', help="Option to Specify DFA file")
    parser.add_argument('REGEX', help="Regex file Location")
    parser.add_argument('INPUT', help="Input file Location")
    args = parser.parse_args()
    linematch()


def regexextract():
    inputfile = open("input.txt", "r")


def linematch():
    inputfile = open("input.txt", "r")
    regex = re.compile(r'^apple$')
    for line in inputfile:
        matches = regex.findall(line)
        for word in matches:
            print(word)


if __name__ == "__main__":
    run()
