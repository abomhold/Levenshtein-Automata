class LevenshteinAutomaton:
    def __init__(self, string, max_edits):
        self._string = string
        self._max_edits = max_edits
        self._states = {}
        self._transitions = []
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
        return set(c for (i, c) in enumerate(self._string) if state[i] <= self._max_edits)

    def build(self, state):
        if state in self._states:
            return self._states[state]

        state_id = self._counter
        self._counter += 1
        self._states[state] = state_id

        if self.is_match(state):
            self._accepting.add(state_id)

        for c in self.transitions(state) | {'*'}:
            new_state = self.step(state, c)
            if self.can_match(new_state):
                new_state_id = self.build(new_state)
                self._transitions.append((state_id, new_state_id, c))

        return state_id

    def query(self, string):
        state = self.start()
        state_id = self._states[state]
        for c in string:
            next_state_id = None
            for from_id, to_id, trans_char in self._transitions:
                if from_id == state_id and (trans_char == c or trans_char == '*'):
                    next_state_id = to_id
                    break
            if next_state_id is None:
                return False
            state_id = next_state_id
        return state_id in self._accepting

# Example usage
if __name__ == "__main__":
    automaton = LevenshteinAutomaton("hello", 2)

    test_strings = ["hello", "helo", "world", "hell", "helloo", "hallo"]
    for test in test_strings:
        result = automaton.query(test)
        print(f"'{test}' is within 2 edits of 'hello': {result}")








# class LevenshteinAutomaton:
#     def __init__(self, target, alphabet, max_edits):
#         self._target = target
#         self._alphabet = alphabet
#         self._max_edits = max_edits
#         self._states = {}
#         self._transitions = []
#         self._accepting = set()
#         self._counter = 0
#         # self.build(self.start())
#
#     def start(self):
#         return tuple(range(len(self._target) + 1))
#
#     def is_match(self, state):
#         return state[-1] <= self._max_edits
#
#     def can_match(self, state) -> bool:
#         return min(state) <= self._max_edits
#
#     def step(self, state, c) -> tuple[int, ...]:
#         new_state = [state[0] + 1]
#         for i in range(len(state) - 1):
#             cost = 0 if self._target[i] == c else 1
#             new_state.append(min(new_state[i] + 1, state[i] + cost, state[i + 1] + 1))
#         return tuple(min(x, self._max_edits + 1) for x in new_state)
#
#     def build(self, state) -> int:
#         if state in self._states:
#             return self._states[state]
#
#         self._states[state] = self._counter
#         self._counter += 1
#
#         if self.is_match(state):
#             self._accepting.add(self._states[state])
#
#         for c in self._alphabet | {'*'}:
#             new_state = self.step(state, c)
#             if self.can_match(new_state):
#                 new_state_id = self.build(new_state)
#                 self._transitions.append((self._states[state], new_state_id, c))
#
#         return self._states[state]
#
#     # def query(self, string):
#     #     if self._accepting.__contains__(string):
#     #         return True
#     #     return False
#
#     def query(self, string):
#         state = self.start()
#         for c in string:
#             state = self.step(state, c)
#             if not self.can_match(state):
#                 return False
#         return self.is_match(state)
#
#
# # Example usage:
# if __name__ == "__main__":
#     target = "hello"
#     alphabet = set("abcdefghijklmnopqrstuvwxyz")
#     max_edits = 2
#
#     automaton = LevenshteinAutomaton(target, alphabet, max_edits)
#     print(automaton)
#     test_strings = ["hello", "helo", "world", "hell", "helloo", "hallo"]
#     for test in test_strings:
#         result = automaton.query(test)
#         print(f"'{test}' is within {max_edits} edits of '{target}': {result}")
