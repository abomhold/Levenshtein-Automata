import random
from src import dyn

# import NFA

# Standard Alphabet
# Σ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Binary Alphabet
# Σ = "01"
# DNA Alphabet
# Σ = "ATGC"
# Target String
targets = ["AB", "ABC", "ABCD", "ABCDE", "ABCDEF", "ABCDEFG", "ABCDEFGH"]
distance = 3
CALCULATIONS = 0

# Maximum length of the string
# str_len = len(target)
# Number of strings to generate
str_cnt = 1000
# Maximum number of edits
max_edits = 2


# Example usage
def generate_strings(target: str):
    global str_cnt
    str_len = len(target)
    for _ in range(str_cnt):
        yield "".join(random.choices(target + "?", k=str_len))


def dynamic(target: str, guesses: list[str], max_edits: int) -> (list[bool], int):
    return dyn.solve(target, max_edits, guesses)


def automaton(target: str, test_strings: list[str], max_edits: int) -> (list[bool], int):
    return dyn.solve(target, max_edits, test_strings)


if __name__ == "__main__":
    for TARGETS in targets:
        test_strings = generate_strings(TARGETS)
        results, calcs = dynamic(TARGETS, test_strings, max_edits)
        print(f"DYN: {results}")
        print(f"DYN: {calcs}")

        results, calcs = automaton(TARGETS, test_strings, max_edits)
        print(f"AUTO: {results}")
        print(f"AUTO: {calcs}")

        print("")
#
#
# def christofides(index):
#     return ch.solve(PATHS[index])
#
#
# def nearest_neighbor(index):
#     return nn.solve(PATHS[index])
#
#
# def multi_proc_loop():
#     with multiprocessing.Pool() as pool:
#         chris_results = pool.map(christofides, range(number_of_paths))
#         held_results = pool.map(held_karp, range(number_of_paths))
#         nearest_results = pool.map(nearest_neighbor, range(number_of_paths))
#     return chris_results, held_results, nearest_results
#
#
#
