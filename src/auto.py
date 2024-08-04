from collections import defaultdict
# from src import utils
from src.utils import targets, max_edits, generate_strings


class LevenshteinAutomaton:
    def __init__(self, string, edits_dist):
        self.Calculations = 0
        self._string = string
        self._max_edits = edits_dist
        self._states = {}
        self._transitions = defaultdict(dict)
        self._accepting = set()
        self._counter = 0
        self.build(self.start())

    def start(self):
        return tuple(range(len(self._string) + 1))

    def is_match(self, state):
        return state[-1] <= self._max_edits

    def can_match(self, state):
        return min(state) <= self._max_edits

    def step(self, state, c):
        new_state = [state[0] + 1]
        for i in range(len(state) - 1):
            cost = 0 if self._string[i] == c else 1
            new_state.append(min(new_state[i] + 1, state[i] + cost, state[i + 1] + 1))
        return tuple(min(x, self._max_edits + 1) for x in new_state)

    def transitions(self, state):
        result_set = set()
        for i, c in enumerate(self._string):
            self.Calculations += 1
            if state[i] <= self._max_edits:
                result_set.add(c)
        return result_set

    def build(self, state):
        self.Calculations += 1
        if state in self._states:
            return self._states[state]

        state_id = self._counter
        self._counter += 1
        self._states[state] = state_id
        self._transitions[state_id] = {}

        if self.is_match(state):
            self._accepting.add(state_id)

        for c in self.transitions(state) | {'*'}:
            new_state = self.step(state, c)
            if self.can_match(new_state):
                new_state_id = self.build(new_state)
                self._transitions[state_id][c] = new_state_id

        return state_id

    def query(self, string) -> (bool, int):
        state_id = self._states[self.start()]
        for c in string:
            self.Calculations += 1
            if c in self._transitions[state_id]:
                state_id = self._transitions[state_id][c]
            elif '*' in self._transitions[state_id]:
                state_id = self._transitions[state_id]['*']
            else:
                return False
        return state_id in self._accepting

    # def build(self, state):
    #     # self.Calculations += 1
    #     if state in self._states:
    #         return self._states[state]
    #     state_id = self._counter
    #     self._counter += 1
    #     self._states[state] = state_id
    #     if self.is_match(state):
    #         self._accepting.add(state_id)
    #     transitions = self.transitions(state)
    #     for c in transitions | {'*'}:
    #         new_state = self.step(state, c)
    #         if self.can_match(new_state):
    #             new_state_id = self.build(new_state)
    #             self._transitions[state_id][c] = new_state_id
    #     return state_id

    # def query(self, string):
    #     state_id = self._states[self.start()]
    #     for c in string:
    #         self.Calculations += 1
    #         if c in self._transitions[state_id]:
    #             state_id = self._transitions[state_id][c]
    #         elif '*' in self._transitions[state_id]:
    #             state_id = self._transitions[state_id]['*']
    #         else:
    #             return False
    #     return state_id in self._accepting


def solve(target: str, max_edits: int, test_strings: list[str]) -> tuple[list[bool], int]:
    auto = LevenshteinAutomaton(target, max_edits)
    results = []
    for string in test_strings:
        result = auto.query(string)
        results.append(result)

    return results, auto.Calculations


if __name__ == "__main__":
    for target in targets:
        test_strings = generate_strings(target, 100)
        results, calcs = solve(targets, max_edits, test_strings)
        # print(results)
        print(calcs)

# def solve(target: str, max_edits: int, test_strings: list[str]) -> tuple[list[bool], int]:
#     auto = LevenshteinAutomaton(target, max_edits)
#     results = []
#     for string in test_strings:
#         results.append(auto.query(string))
#     return results, auto.Calculations
#
#
# if __name__ == "__main__":
#     from src.utils import targets, max_edits, generate_strings
#
#     for target in targets:
#         test_strings = generate_strings(target, 100)
#         results, calcs = solve(targets, max_edits, test_strings)
#         # print(results)
#         print(calcs)

#
#
# class LevenshteinAutomaton:
#     def __init__(self, string, edits_dist):
#         self._string = string
#         self._max_edits = edits_dist
#         self._states = {}
#         self._transitions = {}
#         self._accepting = set()
#         self._counter = 0
#         self._calculations = 0
#         self.build(self.start())
#
#     def get_calcs(self):
#         return self._calculations
#
#     def start(self):
#         return tuple(range(len(self._string) + 1))
#
#     def is_match(self, state):
#         return state[-1] <= self._max_edits
#
#     def can_match(self, state):
#         return min(state) <= self._max_edits
#
#     def step(self, state, c):
#         new_state = [state[0] + 1]
#         for i in range(len(state) - 1):
#             cost = 0 if self._string[i] == c else 1
#             new_state.append(min(new_state[i] + 1, state[i] + cost, state[i + 1] + 1))
#         return tuple(min(x, self._max_edits + 1) for x in new_state)
#
#     def transitions(self, state):
#         self._calculations += 1
#         return set(c for (i, c) in enumerate(self._string) if state[i] <= self._max_edits)
#
#     def build(self, state):
#         # self._calculations += 1
#         if state in self._states:
#             return self._states[state]
#
#         state_id = self._counter
#         self._counter += 1
#         self._states[state] = state_id
#         self._transitions[state_id] = {}
#
#         if self.is_match(state):
#             self._accepting.add(state_id)
#
#         for c in self.transitions(state) | {'*'}:
#             new_state = self.step(state, c)
#             if self.can_match(new_state):
#                 new_state_id = self.build(new_state)
#                 self._transitions[state_id][c] = new_state_id
#
#         return state_id
#
#     def query(self, string) -> (bool, int):
#         state_id = self._states[self.start()]
#         # print(self._transitions)
#         for c in string:
#             # self._calculations += 1
#             if c in self._transitions[state_id]:
#                 state_id = self._transitions[state_id][c]
#             elif '*' in self._transitions[state_id]:
#                 state_id = self._transitions[state_id]['*']
#             else:
#                 return False, self._calculations
#         return state_id in self._accepting, self._calculations
#
