import random

# import NFA

# Standard Alphabet
Σ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Binary Alphabet
# Σ = "01"
# DNA Alphabet
# Σ = "ATGC"
# Target String
σ = "AUSTINBOMHOLD"

CALCULATIONS = 0

# Maximum length of the string
n = 10
# Number of strings to generate
m = 10000


def lev_dyn(str1, str2):
    m = len(str1)
    n = len(str2)
    global CALCULATIONS
    CALCULATIONS = 0

    # Initialize a matrix to store the edit distances
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize the first row and column with values from 0 to m and 0 to n respectively
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the matrix using dynamic programming to compute edit distances
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            CALCULATIONS += 1
            if str1[i - 1] == str2[j - 1]:
                # Characters match, no operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Characters don't match, choose minimum cost among insertion, deletion, or substitution
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

    # Return the edit distance between the strings
    return dp[m][n], CALCULATIONS


# Run if main
def generate_strings(count: int):
    for i in range(count + 1):
        # Generate a random string of length n
        yield "".join(random.choices(Σ, k=random.randint(1, n)))
