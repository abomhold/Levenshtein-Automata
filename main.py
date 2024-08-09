import time

from src import dyn
from src import auto
from src.utils import generate_strings, targets, max_edits

str_cnt_exp = 5


def dynamic(target: str, guesses: list[str], max_edits: int) -> (list[bool], int):
    return dyn.solve(target, max_edits, guesses)


def automaton(target: str, test_strings: list[str], max_edits: int) -> (list[bool], int):
    return auto.solve(target, max_edits,
                      test_strings)


# Define the multi_process loop
if __name__ == "__main__":
    start_time = time.perf_counter()
    results = []
    for exp in range(1, str_cnt_exp):
        str_cnt = 10 ** exp
        for tar in targets:
            test_strings = generate_strings(tar, str_cnt)
            dyn_results = dynamic(tar, test_strings, max_edits)
            auto_results = automaton(tar, test_strings, max_edits)
            results.append((dyn_results, auto_results, tar, str_cnt))
    duration = time.perf_counter() - start_time

    # Gather the results and write them to a CSV file
    with open("../comparison.csv", "w") as f:
        f.write("target,pass_fail,target_size,target_unique,guess_string_count,dyn_calcs,auto_calcs\n")
        for result in results:
            dyn, auto, target, str_cnt = result
            dyn_results, dyn_calcs = dyn
            auto_results, auto_calcs = auto
            f.write(
                f"{target},"
                f" {'PASS' if dyn_results == auto_results else 'FAIL'},"
                f" {len(target)},"
                f" {len(set(target))},"
                f" {str_cnt},"
                f" {dyn_calcs},"
                f" {auto_calcs}\n")
    print(f"Duration: {duration} seconds")
