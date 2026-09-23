from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyfiglet

CSV_PATH = Path(__file__).parent / "counting-data.csv"


def plot_linear_regression() -> None:
    """Read counting-data.csv, fit a simple linear regression, and plot it."""
    data = pd.read_csv(CSV_PATH)
    x = data["Number"].to_numpy()
    y = data["NextNumber"].to_numpy()

    # Fit y = m*x + b using numpy's polynomial fit (degree 1 = linear).
    m, b = np.polyfit(x, y, 1)

    plt.scatter(x, y, label="Data")
    plt.plot(x, m * x + b, color="red", label=f"Fit: y = {m:.2f}x + {b:.2f}")
    plt.xlabel("Number")
    plt.ylabel("NextNumber")
    plt.title("Linear Regression: counting-data.csv")
    plt.legend()
    plt.show()


def main() -> None:
    print(pyfiglet.figlet_format("ARROW H"))
    print(pyfiglet.figlet_format("NATHANIEL R"))
    print(pyfiglet.figlet_format("MAX L"))
    print(pyfiglet.figlet_format("TOM S"))

    plot_linear_regression()


if __name__ == "__main__":
    main()
