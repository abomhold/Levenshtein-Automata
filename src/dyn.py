import random
import src.utils as utils


def lev_dyn(str1, str2, max_edits):
    str1_len = len(str1)
    str2_len = len(str2)

    # If the length difference is greater than max_edits, it can't be within the edit distance
    if abs(str1_len - str2_len) > max_edits:
        return False

    # Initialize previous_row as a list instead of a range
    previous_row = list(range(str2_len + 1))
    current_row = [0] * (str2_len + 1)

    for i in range(1, str1_len + 1):
        current_row[0] = i
        for j in range(1, str2_len + 1):
            if str1[i - 1] == str2[j - 1]:
                current_row[j] = previous_row[j - 1]
            else:
                current_row[j] = 1 + min(previous_row[j], current_row[j - 1], previous_row[j - 1])

        # If the minimum value in the current row is greater than max_edits, break early
        if min(current_row) > max_edits:
            return False

        # Swap rows
        previous_row, current_row = current_row, previous_row

    # Check if the last computed edit distance is within max_edits
    return previous_row[str2_len] <= max_edits


if __name__ == "__main__":
    target = utils.σ
    max_edits = 2

    for test_string in utils.generate_strings():
        result = lev_dyn(target, test_string, max_edits)
        print(f"'{test_string}' is within {max_edits} edits of '{target}': {result}")
