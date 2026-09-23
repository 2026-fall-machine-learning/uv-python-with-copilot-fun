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

    x = data["Number"]
    y = data["NextNumber"]
    x_mean = x.mean()
    y_mean = y.mean()
    centered_x = x - x_mean
    slope = (centered_x * (y - y_mean)).sum() / (centered_x**2).sum()
    intercept = y_mean - slope * x_mean
    predictions = slope * x + intercept

    print(f"Linear regression: NextNumber = {slope:.4f} * Number + {intercept:.4f}")

    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, label="Observed data")
    sorted_indices = x.argsort()
    plt.plot(
        x.iloc[sorted_indices],
        predictions.iloc[sorted_indices],
        color="red",
        label="Linear regression",
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
