# postfix to nfa using thompsons construction, explained more in readme


from graphviz import *


def nfa_conversion(postfix):
    class NfaState:
        def __init__(self, char):
            self.char = char
            self.primary_transition = None
            self.or_split = None

    class NfaPiece:
        def __init__(self, start, unboundfragmentset):
            self.start = start
            self.primary_transition = unboundfragmentset

    def char_symbol(character):
        newtransistion = NfaState(character)
        subnfalist.append(NfaPiece(newtransistion, [newtransistion]))

    def concat_op():
        secondary_fragment = subnfalist.pop()
        nfa_fragment = subnfalist.pop()
        bind_fragment(nfa_fragment.primary_transition, secondary_fragment.start)
        nfa_fragment.primary_transition = secondary_fragment.primary_transition
        subnfalist.append(nfa_fragment)

    def or_operator():
        secondary_fragment = subnfalist.pop()
        nfa_fragment = subnfalist.pop()
        currstate = NfaState(-1)
        currstate.primary_transition = secondary_fragment.start
        currstate.or_split = nfa_fragment.start
        nfa_fragment.start = currstate
        nfa_fragment.primary_transition = nfa_fragment.primary_transition + secondary_fragment.primary_transition
        subnfalist.append(nfa_fragment)

    def splat():
        nfa_fragment = subnfalist.pop()
        currstate = NfaState(-1)
        currstate.primary_transition = nfa_fragment.start
        bind_fragment(nfa_fragment.primary_transition, currstate)
        nfa_fragment.primary_transition = [currstate]
        nfa_fragment.start = currstate
        subnfalist.append(nfa_fragment)

    def bind_fragment(unboundfragmentset, primary_transition):
        for state in unboundfragmentset:
            if state.char == -1:
                state.or_split = primary_transition
            else:
                state.primary_transition = primary_transition

# where unfinished nfa fragments are stored before they get completed

    subnfalist = []
    for index in postfix:
        if index == '.':
            concat_op()
        elif index == '|':
            or_operator()
        elif index == '*':
            splat()
        else:
            char_symbol(index)
    if subnfalist:
        final_fragment = subnfalist.pop()
        bind_fragment(final_fragment.primary_transition, NfaState(-2))
        return final_fragment.start
    return NfaState(-2)

# the library graphviz is used to acheiv graphical representations - explained in readme


def convert_dot_graphviz_nfa(nfa, n):
    index = 0
    queue = []
    state = nfa
    queue.append(state)
    nfastates = {}
    nfastates[state] = 'q' + str(index)
    graphviznfa = Digraph(comment="NFA", graph_attr={'rankdir': 'LR'}, node_attr={'shape': 'circle'})

    while queue:
        state = queue.pop()
        if state.primary_transition is not None and state.primary_transition not in nfastates:
            index = index + 1
            queue.append(state.primary_transition)
            nfastates[state.primary_transition] = 'q' + str(index)
        if state.or_split is not None and state.or_split not in nfastates:
            index = index + 1
            queue.append(state.or_split)
            nfastates[state.or_split] = 'q' + str(index)
        if state.char is -2:
            graphviznfa.node(nfastates[state], shape='doublecircle')
        elif state.char is not -1:
            graphviznfa.node(nfastates[state])
            graphviznfa.edge(nfastates[state], nfastates[state.primary_transition], state.char)
        elif state.char is -1:
            graphviznfa.edge(nfastates[state], nfastates[state.primary_transition], 'epsilon')
            graphviznfa.edge(nfastates[state], nfastates[state.or_split], 'epsilon')
    file = open(n, "w")
    file.write(graphviznfa.source)
    file.close()
    graphviznfa.render(n, view=True)
