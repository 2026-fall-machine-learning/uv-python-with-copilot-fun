from pathlib import Path

import matplotlib
import numpy as np
import pyfiglet

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def print_ascii_art() -> None:
    for text in ["ARROW H", "NATHANIEL R", "MAX L", "TOM S"]:
        print(pyfiglet.figlet_format(text))


def load_data() -> tuple[np.ndarray, np.ndarray]:
    csv_path = Path(__file__).with_name("counting-data.csv")
    xs: list[float] = []
    ys: list[float] = []

    with csv_path.open(newline="") as csv_file:
        import csv

        reader = csv.DictReader(csv_file)
        for row in reader:
            xs.append(float(row["Number"]))
            ys.append(float(row["NextNumber"]))

    return np.asarray(xs, dtype=float), np.asarray(ys, dtype=float)


def main() -> None:
    print_ascii_art()

    x_values, y_values = load_data()
    slope, intercept = np.polyfit(x_values, y_values, 1)
    prediction = slope * x_values + intercept

    figure, axis = plt.subplots(figsize=(8, 6))
    axis.scatter(x_values, y_values, color="blue", label="Data points")
    axis.plot(x_values, prediction, color="red", linewidth=2, label=f"Regression: y = {slope:.2f}x + {intercept:.2f}")
    axis.set_xlabel("Number")
    axis.set_ylabel("Next Number")
    axis.set_title("Linear Regression of counting-data.csv")
    axis.grid(True, linestyle="--", alpha=0.4)
    axis.legend()

    output_path = Path(__file__).with_name("regression_plot.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    print(f"\nSaved regression plot to {output_path}")
    plt.close(figure)


if __name__ == "__main__":
    main()
