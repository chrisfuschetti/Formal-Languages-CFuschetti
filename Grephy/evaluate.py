def evaluate_dfa(dfa, infile):
    print("\nMATCHES FOUND FROM DFA EVALUATION: ")
    f = open(infile, "r")
    lines = f.read().splitlines()
    f.close()
    for line in lines:
        current_state = dfa.start
        for char in line:
            if char in current_state.transitions:
                current_state = current_state.transitions[char]
            else:
                current_state = None
                break
        if current_state and current_state.accept_reject == True:
            print(line)
