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
