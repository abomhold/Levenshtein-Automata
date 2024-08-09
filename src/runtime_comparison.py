import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

min_nodes: int = 4
max_nodes: int = 14


def generate_1_plot() -> None:
    x_values = ["AB", "ABC", "ABCD", "ABCDE", "ABCDEF", "ABCDEFG", "ABCDEFGH", "ABCDEFGHI", "ABCDEFGHIJ", "ABCDEFGHIJK"]
    dynamic_data = [40, 90, 160, 225, 240, 273, 328, 342, 350, 396]
    auto_data = [46, 108, 207, 334, 483, 671, 888, 1134, 1415, 1731]

    fig, ax = plt.subplots()
    plt.plot(x_values, dynamic_data, label='Dynamic Programming', marker='o')
    plt.plot(x_values, auto_data, label='Automaton', marker='s')
    plt.plot(x_values, [x + 40 for x in range(1, 11)], label='n', color='grey', linestyle=':')
    plt.plot(x_values, [x ** 2 + 40 for x in range(1, 11)], label='n²', color='grey', linestyle='--')
    plt.plot(x_values, [2 ** x + 40 for x in range(1, 11)], label='2ⁿ', color='grey', linestyle='-.')
    # plt.plot(x_values, [math.factorial(x) + 40 for x in range(1, 11)], label='3ⁿ', color='grey', linestyle='-.')

    ax.set(
        xlabel='String Length',
        ylabel='Number of Calculations',
        title='Number of Calculations vs. Target (n=10)',
        xmargin=.03,
    )
    ax.set_yscale('symlog', base=2)
    fig.set_size_inches(12, 8)
    fig.legend(loc='upper left')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()
    plt.close()


def generate_2_plot() -> None:
    x_values = ["AB", "ABA", "ABAB", "ABABA", "ABABAB", "ABABABA", "ABABABAB", "ABABABABA", "ABABABABAB", "ABABABABABA"]
    dynamic_data = [40, 90, 160, 250, 360, 490, 584, 783, 840, 935]
    auto_data = [46, 99, 180, 290, 431, 599, 786, 1021, 1256, 1528]

    fig, ax = plt.subplots()
    plt.plot(x_values, dynamic_data, label='Dynamic Programming', marker='o')
    plt.plot(x_values, auto_data, label='Automaton', marker='s')
    plt.plot(x_values, [x + 40 for x in range(1, 11)], label='n', color='grey', linestyle=':')
    plt.plot(x_values, [x ** 2 + 40 for x in range(1, 11)], label='n²', color='grey', linestyle='--')
    plt.plot(x_values, [2 ** x + 40 for x in range(1, 11)], label='2ⁿ', color='grey', linestyle='-.')

    ax.set(
        xlabel='String Length',
        ylabel='Number of Calculations',
        title='Number of Calculations vs. Target (n=10)',
        xmargin=.03,
    )
    # ax.set_yscale('log', base=2)
    # ax.set_xscale('log', base=2)
    ax.set_yscale('symlog', base=2)

    fig.set_size_inches(12, 8)
    fig.legend(loc='upper left')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()
    plt.close()


def generate_3_plot() -> None:
    x_values = [10, 100, 1000, 10000, 100000, 1000000]
    dynamic_data1 = [396, 4004, 39567, 396583, 3969009, 39717348]
    dynamic_data2 = [935, 9339, 95359, 952457, 9500623, 95052067]
    auto_data1 = [1731, 2051, 5293, 37827, 362655, 3613266]
    auto_data2 = [1528, 2213, 9253, 79777, 781892, 7808068]

    fig, ax = plt.subplots()
    ax.plot(x_values, dynamic_data1, label='Dynamic Programming', marker='o')
    ax.plot(x_values, dynamic_data2, label='Dynamic Programming2', marker='o')
    ax.plot(x_values, auto_data1, label='Automaton', marker='s')
    ax.plot(x_values, auto_data2, label='Automaton2', marker='s')
    ax.plot(x_values, [x for x in x_values], label='n', color='grey', linestyle=':')
    ax.plot(x_values, [x * math.log(x, 2) for x in x_values], label='nlg(n)', color='grey', linestyle='-.')

    ax.set(
        xlabel='String Length',
        ylabel='Number of Calculations',
        title='Number of Calculations vs. Target (n=10)',
        xmargin=.03,
    )

    ax.set_yscale('symlog', base=2)
    ax.set_xscale('symlog', base=2)
    fig.set_size_inches(12, 8)
    fig.legend(loc='upper left')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()
    plt.close()


# def generate_4_plot() -> None:
#     x_values = [10, 100, 1000, 10000, 100000, 1000000]
#
#     fig, ax = plt.subplots()
#     ax.plot(x_values, auto_data2, label='Automaton', marker='s')
#     ax.plot(x_values, [x for x in x_values], label='n', color='grey', linestyle=':')
#     ax.plot(x_values, [x ** 2 for x in x_values], label='n²', color='grey', linestyle='--')
#     ax.plot(x_values, [x * math.log(x, 2) for x in x_values], label='nlg(n)', color='grey', linestyle='-.')
#
#     ax.set(
#         xlabel='Number of Guess Strings',
#         ylabel='Number of Calculations',
#         title='Number of Calculations vs. Number of Guess Strings (n="ABABABABABA")',
#         xmargin=.03,
#     )
#
#     ax.set_yscale('log', base=2)
#     ax.set_xscale('log', base=2)
#     fig.set_size_inches(12, 8)
#     fig.legend()
#     plt.grid(True)
#     plt.xticks(rotation=45)
#     plt.show()
#     plt.close()


if __name__ == '__main__':
    generate_1_plot()
    generate_2_plot()
    generate_3_plot()
    # generate_4_plot()
