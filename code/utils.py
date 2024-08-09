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
