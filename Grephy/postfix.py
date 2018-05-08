import sys


def postfix_conversion(regex, alphabet):
    operators = ['(', ')', '|', '*']
    charcount = 0
    orcount = 0
    parenscopestack = []
    postfixlist = []

    for char in regex:
        if char not in alphabet and char not in operators:
            sys.exit('A Character in your REGEX is not in the alphabet')
        if char == '(':
            if charcount == 2:
                postfixlist.append('.')
                charcount = 1
            parenscopestack.append((charcount, orcount))
            charcount = 0
            orcount = 0
        elif char == ')':
            if charcount == 2:
                postfixlist.append('.')
            if orcount > 0:
                postfixlist.append('|' * orcount)
            charcount, orcount = parenscopestack.pop()
            charcount += 1
        elif char == '|':
            if charcount == 2:
                postfixlist.append('.')
            charcount = 0
            orcount += 1
        elif char == '*':
            postfixlist.append(char)
        else:
            if charcount == 2:
                postfixlist.append('.')
                charcount -= 1
            postfixlist.append(char)
            charcount += 1

    if charcount == 2:
        postfixlist.append('.')
    if orcount > 0:
        postfixlist.append('|' * orcount)
    print("\nRegex Converted to Postfix and Concatenation Represented by . :")
    print(*postfixlist)
    return postfixlist
