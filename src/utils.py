import random

# import NFA

# Standard Alphabet
# Σ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Binary Alphabet
# Σ = "01"
# DNA Alphabet
Σ = "ATGC"
# Target String
σ = "ATGC"

distance = 2

CALCULATIONS = 0

# Maximum length of the string
str_len = len(σ) + 3
# Number of strings to generate
str_cnt = 10000


# Example usage
def generate_strings():
    global str_len, str_cnt
    for _ in range(str_cnt):
        yield "".join(random.choices(Σ, k=random.randint(1, str_len)))
