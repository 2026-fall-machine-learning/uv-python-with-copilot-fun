import csv
from pathlib import Path

import matplotlib.pyplot as plt
import pyfiglet


DATA_FILE = Path(__file__).with_name("counting-data.csv")


def load_data(path: Path) -> tuple[list[float], list[float]]:
    with path.open(newline="", encoding="utf-8") as csv_file:
        rows = csv.DictReader(csv_file)
        if rows.fieldnames is None or {"Number", "NextNumber"} - set(rows.fieldnames):
            raise ValueError("CSV must contain Number and NextNumber columns")

        data = [(float(row["Number"]), float(row["NextNumber"])) for row in rows]

    if len(data) < 2:
        raise ValueError("CSV must contain at least two data points")

    x_values, y_values = zip(*data)
    return list(x_values), list(y_values)


def linear_regression(x_values: list[float], y_values: list[float]) -> tuple[float, float]:
    x_mean = sum(x_values) / len(x_values)
    y_mean = sum(y_values) / len(y_values)
    denominator = sum((x - x_mean) ** 2 for x in x_values)
    if denominator == 0:
        raise ValueError("The Number values must not all be the same")

    slope = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, y_values))
    slope /= denominator
    intercept = y_mean - slope * x_mean
    return slope, intercept


def plot_regression(path: Path = DATA_FILE) -> None:
    x_values, y_values = load_data(path)
    slope, intercept = linear_regression(x_values, y_values)
    line_x = [min(x_values), max(x_values)]
    line_y = [slope * x + intercept for x in line_x]

    plt.scatter(x_values, y_values, label="Data")
    plt.plot(line_x, line_y, color="red", label=f"y = {slope:.2f}x + {intercept:.2f}")
    plt.xlabel("Number")
    plt.ylabel("NextNumber")
    plt.title("NextNumber Linear Regression")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()


def main() -> None:
    print(pyfiglet.figlet_format("ARROW H"))
    print(pyfiglet.figlet_format("NATHANIEL R"))
    print(pyfiglet.figlet_format("MAX L"))
    print(pyfiglet.figlet_format("TOM S"))
    plot_regression()


if __name__ == "__main__":
    main()
