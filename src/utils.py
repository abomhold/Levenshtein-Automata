import multiprocessing
import random
import time
import multiprocessing
from tqdm import tqdm


max_edits = 2
targets = ["AB", "ABC", "ABCD", "ABCDE",
           "ABCDEF", "ABCDEFG", "ABCDEFGH", "ABCDEFGHI",
           "ABCDEFGHIJ", "ABCDEFGHIJK",
           "ABA", "ABAB", "ABABA", "ABABAB",
           "ABABABA", "ABABABAB", "ABABABABA", "ABABABABAB",
           "ABABABABABA"]


def generate_strings(target: str, str_cnt: int) -> list[str]:
    strs = []
    for _ in range(str_cnt):
        strs.append("".join(random.choices(target, k=len(target))))
    return strs

#
# # Define functions to be run in parallel
# def dynamic(target: str, guesses: list[str],
#             max_edits: int) -> (list[bool], int):
#     return dyn.solve(target, max_edits, guesses)
#
#
# def automaton(target: str, test_strings: list[str],
#               max_edits: int) -> (list[bool], int):
#     return auto.solve(target, max_edits,
#                       test_strings)
#
#
# # Define the multi_process loop
# def main():
#     # List of targets and parameters to be processed
#     # in parallel
#     global targets, max_edits
#     results = []
#     for exp in range(1, str_cnt_exp):
#         str_cnt = 10 ** exp
#         for tar in targets:
#             test_strings = generate_strings(tar, str_cnt)
#             dyn_results = dynamic(tar, test_strings, max_edits)
#             auto_results = automaton(tar, test_strings, max_edits)
#             results.append((dyn_results, auto_results, tar, str_cnt))
#             print(tar)
#
#     # Gather the results and write them to a CSV file
#     with open("../data/comparison.csv", "w") as f:
#         f.write("target,pass_fail,target_size, target_unique, guess_string_count,dyn_calcs,auto_calcs\n")
#         for result in results:
#             dyn, auto, target, str_cnt = result
#             dyn_results, dyn_calcs = dyn
#             auto_results, auto_calcs = auto
#             f.write(
#                 f"{target},{'PASS' if dyn_results == auto_results else 'FAIL'},{len(target)},{len(set(target))},{str_cnt},{dyn_calcs},{auto_calcs}\n")
#
#
# if __name__ == "__main__":
#     start_time = time.time()
#     main()
#     duration = time.time() - start_time
#     print(f"Duration: {duration} seconds")
