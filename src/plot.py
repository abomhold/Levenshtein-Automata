import math

import matplotlib.pyplot as plt


def generate_1_plot() -> None:
    x_values = range(1, 11)
    dynamic_data1 = [40, 90, 160, 225, 240, 273, 328, 342, 350, 396]
    auto_data1 = [46, 108, 207, 334, 483, 671, 888, 1134, 1415, 1731]
    dynamic_data2 = [40, 90, 160, 250, 360, 490, 584, 783, 840, 935]
    auto_data2 = [46, 99, 180, 290, 431, 599, 786, 1021, 1256, 1528]

    fig, ax = plt.subplots()
    plt.plot(x_values, dynamic_data1, color='red', label='Dynamic Programming (Pattern 1)', marker='o')
    plt.plot(x_values, dynamic_data2, color='orange', label='Dynamic Programming (Pattern 2)', marker='o')
    plt.plot(x_values, auto_data1, color='blue', label='Automaton (Pattern 1)', marker='s')
    plt.plot(x_values, auto_data2, color='purple', label='Automaton (Pattern 2)', marker='s')
    plt.plot(x_values, [x ** 3 + 40 for x in range(1, 11)], label='n³', color='grey', linestyle=':')
    plt.plot(x_values, [math.log(x) * x ** 3 + 40 for x in range(1, 11)], label='n³lg(n)', color='grey', linestyle=':')

    ax.set(
        xlabel='Target Length',
        ylabel='Number of Calculations',
        title='Number of Calculations vs. Target Length (Guess Strings = 10)',
        xmargin=.03,
    )
    fig.set_size_inches(12, 8)
    fig.legend(loc='upper left')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig('../data/plot1.png')
    plt.show()
    plt.close()


def generate_2_plot() -> None:
    x_values = [10, 100, 1000, 10000, 100000, 1000000]
    dynamic_data1 = [396, 4004, 39567, 396583, 3969009, 39717348]
    dynamic_data2 = [935, 9339, 95359, 952457, 9500623, 95052067]
    auto_data1 = [1731, 2051, 5293, 37827, 362655, 3613266]
    auto_data2 = [1528, 2213, 9253, 79777, 781892, 7808068]

    fig, ax = plt.subplots()
    plt.plot(x_values, dynamic_data1, color='red', label='Dynamic Programming (Pattern 1)', marker='o')
    plt.plot(x_values, dynamic_data2, color='orange', label='Dynamic Programming (Pattern 2)', marker='o')
    plt.plot(x_values, auto_data1, color='blue', label='Automaton (Pattern 1)', marker='s')
    plt.plot(x_values, auto_data2, color='purple', label='Automaton (Pattern 2)', marker='s')
    ax.plot(x_values, [x for x in x_values], label='n', color='grey', linestyle=':')
    ax.plot(x_values, [x * math.log(x, 2) for x in x_values], label='nlg(n)', color='grey', linestyle=':')
    ax.plot(x_values, [x * (math.log(x, 2) ** 2) for x in x_values], label='nlg(n)²', color='grey', linestyle=':')

    ax.set(
        xlabel='Number of Guess Strings',
        ylabel='Number of Calculations',
        title='Number of Calculations vs. Number of Guess Strings (Target Length = 10)',
        xmargin=.03,
    )

    ax.set_yscale('log', base=2)
    ax.set_xscale('log', base=2)
    fig.set_size_inches(12, 8)
    fig.legend(loc='upper left')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig('../data/plot2.png')
    plt.show()
    plt.close()


if __name__ == '__main__':
    generate_1_plot()
    generate_2_plot()
