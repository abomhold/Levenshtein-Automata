import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_data():
    data = pd.read_csv("../data/comparison.csv")
    data = data.dropna()
    return data


def plot_data(data):
    data = data.groupby("target")
    fig, ax = plt.subplots()
    ax.legend()
    plt.show()


if __name__ == "__main__":
    data = load_data()
    print(data)
    plot_data(data)

