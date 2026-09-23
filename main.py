from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyfiglet

CSV_PATH = Path(__file__).parent / "counting-data.csv"


def plot_linear_regression() -> None:
    """Read counting-data.csv, fit a simple linear regression, and plot it.

    Uses a poor man's train/test split (80/20, fixed seed) so the line is
    fit only on the training rows, then draws the fitted line extended 100
    units past the min/max of x in both directions.
    """
    data = pd.read_csv(CSV_PATH)

    # Poor man's train/test split: shuffle with a fixed seed for
    # reproducibility, then take the first 80% as train, rest as test.
    train = data.sample(frac=0.8, random_state=42)
    test = data.drop(train.index)

    x_train = train["Number"].to_numpy()
    y_train = train["NextNumber"].to_numpy()
    x_test = test["Number"].to_numpy()
    y_test = test["NextNumber"].to_numpy()

    # Fit y = m*x + b using numpy's polynomial fit (degree 1 = linear),
    # trained on the training split only.
    m, b = np.polyfit(x_train, y_train, 1)

    # Extend the fitted line 100 units beyond the data's min/max x.
    x_all = data["Number"].to_numpy()
    line_x = np.array([x_all.min() - 100, x_all.max() + 100])
    line_y = m * line_x + b

    plt.scatter(x_train, y_train, label="Train")
    plt.scatter(x_test, y_test, label="Test")
    plt.plot(line_x, line_y, color="red", label=f"Fit (train): y = {m:.2f}x + {b:.2f}")
    plt.xlabel("Number")
    plt.ylabel("NextNumber")
    plt.title("Linear Regression: counting-data.csv (train/test split)")
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
