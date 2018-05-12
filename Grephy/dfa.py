# nfa to dfa through subset construction, more info in read me
# graphviz is also used here


from graphviz import *


def dfa_conversion(nfa, alphabet):
    class DfaState:
        def __init__(self, states, accept_reject=False):
            self.states = states
            self.transitions = {}
            self.accept_reject = accept_reject

    class FullDfa:
        def __init__(self):
            self.setofstates = set()
            self.start = None

        def availible_transitions(self, character, states):
            transitions = set()
            for state in states:
                if state.char == character:
                    transitions.add(state.primary_transition)
            return transitions

        def eclosure(self, nfa_states):
            epsilonset = set()
            nfa_states_temp = nfa_states.copy()
            accept_reject = False
            for state in nfa_states_temp:
                if state.char is -1:
                    epsilonset.add(state.primary_transition)
                    epsilonset.add(state.or_split)
                    nfa_states.add(state)
                while epsilonset:
                    current = epsilonset.pop()
                    if current.char is -1:
                        epsilonset.add(current.primary_transition)
                        epsilonset.add(current.or_split)
                    else:
                        nfa_states.add(current)
            for dstate in self.setofstates:
                if dstate.states == nfa_states:
                    return dstate
            for state in nfa_states:
                if state.char == -2:
                    accept_reject = True
            result = DfaState(nfa_states, accept_reject)
            return result

    dfa = FullDfa()
    nfastack = []
    addstate = dfa.eclosure(set([nfa]))
    nfastack.append(addstate)
    dfa.setofstates.add(addstate)
    dfa.start = addstate
# a stack is needed to add all the new transitions to the old nfa states

    while nfastack:
        current_state = nfastack.pop()
        for char in alphabet:
            next_nfa_states = dfa.availible_transitions(char, current_state.states)
            if next_nfa_states:
                addstate = dfa.eclosure(next_nfa_states)
                current_state.transitions[char] = addstate
                if addstate not in dfa.setofstates:
                    nfastack.append(addstate)
                    dfa.setofstates.add(addstate)

    return dfa


def convert_dot_graphviz_dfa(dfa, d):
    graphvizdfa = Digraph(comment="DFA", graph_attr={'rankdir': 'LR'}, node_attr={'shape': 'circle'})
    index = 1
    for state in dfa.setofstates:
        if state.accept_reject is True:
            graphvizdfa.node(str(state), 'q' + str(index), shape='doublecircle')
            ++index
        elif state is dfa.start:
            graphvizdfa.node(str(dfa.start), 'q0')
        else:
            graphvizdfa.node(str(state), 'q' + str(index))
            ++index
        if state.transitions:
            for char in state.transitions:
                graphvizdfa.edge(str(state), str(state.transitions[char]), char)

    file = open(d, "w")
    file.write(graphvizdfa.source)
    file.close()
    graphvizdfa.render(d, view=True)
