import string_generator
import time

CALCULATIONS = 0


class lev:
    _states = {}
    _transitions = []
    _accepting = []
    _counter = [0]
    _string = ""
    _max_edits: int = 2

    def __init__(self, string):
        self._string: str = string
        # self.build(self.start())

    def transitions(self, state):
        return set(c for (i, c) in enumerate(self._string) if state[i] <= self._max_edits)

    def build(self, state):
        key = tuple(state)  # lists can't be hashed in Python so convert to a tuple

        if key in self._states:
            return self._states[key]

        i = self._counter[0]
        self._counter[0] += 1
        self._states[key] = i

        if self.is_match(state):
            self._accepting.append(i)

        for c in lev.transitions(self, state) | {'*'}:
            newstate = self.step(state, c)
            j = self.build(newstate)
            self._transitions.append((i, j, c))

        return i

    def start(self):
        return range(len(self._string) + 1)

    def is_match(self, state):
        # print(int(list(state)[-1]))
        # print(self._max_edits)
        return list(state)[-1] <= self._max_edits

    def step(self, state, c):
        new_state = [state[0] + 1]
        for i in range(len(state) - 1):
            cost = 0 if self._string[i] == c else 1
            new_state.append(min(new_state[i] + 1, state[i] + cost, state[i + 1] + 1))
        return [min(x, self._max_edits + 1) for x in new_state]

    def can_match(self, state):
        return min(state) <= self._max_edits


if __name__ == "__main__":
    target = "ATCGGCTAGA"
    s2 = string_generator.generate_strings(1000)
    DYN_TOTAL = 0
    LA_TOTAL = 0
    DYN_WINS = 0
    LA_WINS = 0

    # lev_auto =
    i = lev.build(lev(target), lev(target).start())
    print(i)

    for s in s2:
        d1, DYN_CALC = string_generator.lev_dyn(target, s)
        print(f"Dynamic Programming: {d1}")
        # DYN_TOTAL += DYN_CALC
        d2 = lev_auto[s]
        print(d2)
        # LA_TOTAL += LA_CALC
        if d1 < 3 and d2:
            print(f"TRUE")
        elif d1 >= 3 and not d2:
            print(f"FALSE")
        else:
            print(f"ERROR")

    # start_la = time.perf_counter()
    # for s in s2:
    #     d2, LA_CALC = lev(target, s)
    #     LA_TOTAL += LA_CALC
    #
    # time_la = time.perf_counter() - start_la
    # print(f"Levenshtein Automaton: {time_la}")
    #
    # start_dyn = time.perf_counter()
    # for s in s2:
    #     d1, DYN_CALC = string_generator.lev_dyn(target, s)
    #     DYN_TOTAL += DYN_CALC
    #
    # time_dyn = time.perf_counter() - start_dyn
    # print(f"Dynamic Programming: {time_dyn}")

# def MIN(a, b, c):
# class NFA(object):
#
#     def transitions(self, state, c):
#         raise NotImplementedError()
#
#     def accept(self, state):
#         raise NotImplementedError()
#
#     def initial_states(self, ):
#         raise NotImplementedError()
#
#     def eval(self, input_string):
#         states = self.initial_states()
#         for c in input_string:
#             next_states = set()
#             for state in states:
#                 next_states |= set(self.transitions(state, c))
#             states = next_states
#         for state in states:
#             if self.accept(state):
#                 return True
#
#
# class LevenshteinAutomaton(NFA):
#
#     def __init__(self, query, D=2):
#         self.query = query
#         self.max_D = D
#
#     def transitions(self, state, c):
#         (offset, D) = state
#         if D > 0:
#             yield (offset, D - 1)
#             yield (offset + 1, D - 1)
#         for d in range(min(D + 1, len(self.query) - offset)):
#             global CALCULATIONS
#             CALCULATIONS += 1
#             if c == self.query[offset + d]:
#                 yield offset + d + 1, D - d
#
#     def accept(self, state):
#         (offset, D) = state
#         return len(self.query) - offset <= D
#
#     def initial_states(self, ):
#         return {(0, self.max_D)}
#
#
# def levenshtein(s1, s2, D=2):
#     global CALCULATIONS
#     CALCULATIONS = 0
#     return LevenshteinAutomaton(s2, D).eval(s1), CALCULATIONS
#
