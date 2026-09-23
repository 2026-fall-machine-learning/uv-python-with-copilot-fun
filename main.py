from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import pyfiglet


DATA_FILE = Path(__file__).with_name("counting-data.csv")
PLOT_FILE = Path(__file__).with_name("linear-regression.png")


def print_names() -> None:
    for name in ("ARROW H", "NATHANIEL R", "MAX L", "TOM S"):
        print(pyfiglet.figlet_format(name))


def create_regression_plot() -> None:
    data = pd.read_csv(DATA_FILE)
    required_columns = {"Number", "NextNumber"}
    missing_columns = required_columns.difference(data.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"{DATA_FILE.name} is missing required column(s): {missing}")

    data = data[["Number", "NextNumber"]].apply(pd.to_numeric, errors="coerce").dropna()
    if len(data) < 2:
        raise ValueError("The CSV must contain at least two valid numeric rows.")

    split_index = len(data) // 2
    if split_index < 2 or len(data) - split_index < 1:
        raise ValueError("The CSV must contain enough rows for training and test data.")

    training_data = data.iloc[:split_index]
    test_data = data.iloc[split_index:]
    x_train = training_data["Number"]
    y_train = training_data["NextNumber"]
    x_mean = x_train.mean()
    y_mean = y_train.mean()
    centered_x = x_train - x_mean
    denominator = (centered_x**2).sum()
    if denominator == 0:
        raise ValueError("Training data must contain more than one unique Number value.")

    slope = (centered_x * (y_train - y_mean)).sum() / denominator
    intercept = y_mean - slope * x_mean

    print(f"Linear regression: NextNumber = {slope:.4f} * Number + {intercept:.4f}")

    plt.figure(figsize=(8, 5))
    plt.scatter(
        training_data["Number"],
        training_data["NextNumber"],
        label="Training data",
        color="blue",
    )
    plt.scatter(
        test_data["Number"],
        test_data["NextNumber"],
        label="Test data",
        color="orange",
    )
    line_x = pd.Series([data["Number"].min() - 100, data["Number"].max() + 100])
    line_y = slope * line_x + intercept
    plt.plot(
        line_x,
        line_y,
        color="red",
        label="Training regression line",
    )
    plt.xlabel("Number")
    plt.ylabel("NextNumber")
    plt.title("Linear Regression: Number vs. NextNumber")
    plt.legend()
    plt.tight_layout()
    plt.savefig(PLOT_FILE)
    print(f"Plot saved to: {PLOT_FILE}")
    plt.show()
    plt.close()


def main() -> None:
    print_names()
    create_regression_plot()



if __name__ == "__main__":
    main()
