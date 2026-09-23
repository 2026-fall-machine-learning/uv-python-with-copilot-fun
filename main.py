from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyfiglet


DATA_FILE = Path(__file__).with_name("counting-data.csv")


def print_names() -> None:
    for name in ("ARROW H", "NATHANIEL R", "MAX L", "TOM S"):
        print(pyfiglet.figlet_format(name))


def load_data() -> pd.DataFrame:
    data = pd.read_csv(DATA_FILE)
    required_columns = {"Number", "NextNumber"}
    missing_columns = required_columns - set(data.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise ValueError(f"{DATA_FILE.name} is missing required column(s): {missing}")

    data = data[["Number", "NextNumber"]].apply(pd.to_numeric, errors="coerce")
    if data.isna().any().any():
        raise ValueError("The CSV must contain only numeric values in Number and NextNumber.")
    if len(data) < 2:
        raise ValueError("The CSV must contain at least two numeric data rows.")
    if data["Number"].nunique() < 2:
        raise ValueError("The Number column must contain at least two distinct values.")
    return data


def plot_regression(data: pd.DataFrame) -> None:
    x = data["Number"].to_numpy()
    y = data["NextNumber"].to_numpy()
    slope, intercept = np.polyfit(x, y, 1)
    fitted_y = slope * x + intercept

    print(f"Linear regression: NextNumber = {slope:.3f} * Number + {intercept:.3f}")

    plt.scatter(x, y, label="Observed data")
    order = np.argsort(x)
    plt.plot(x[order], fitted_y[order], color="orange", label="Regression line")
    plt.xlabel("Number")
    plt.ylabel("NextNumber")
    plt.title("Number vs. NextNumber")
    plt.legend()
    plt.tight_layout()
    plt.show()


def main() -> None:
    print_names()
    plot_regression(load_data())



if __name__ == "__main__":
    main()
