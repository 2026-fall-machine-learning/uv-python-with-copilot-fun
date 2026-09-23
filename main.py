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


def split_train_test(x_values: np.ndarray, y_values: np.ndarray, test_fraction: float = 0.2) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    rng = np.random.default_rng(42)
    indices = np.arange(len(x_values))
    rng.shuffle(indices)

    test_size = max(1, int(round(len(x_values) * test_fraction)))
    train_size = len(x_values) - test_size

    train_indices = indices[:train_size]
    test_indices = indices[train_size:]

    return (
        x_values[train_indices],
        y_values[train_indices],
        x_values[test_indices],
        y_values[test_indices],
    )


def main() -> None:
    print_ascii_art()

    x_values, y_values = load_data()
    x_train, y_train, x_test, y_test = split_train_test(x_values, y_values)

    slope, intercept = np.polyfit(x_train, y_train, 1)
    x_domain = np.linspace(x_values.min() - 100, x_values.max() + 100, 400)
    y_domain = slope * x_domain + intercept

    train_predictions = slope * x_train + intercept
    test_predictions = slope * x_test + intercept
    train_error = np.mean(np.abs(y_train - train_predictions))
    test_error = np.mean(np.abs(y_test - test_predictions))

    figure, axis = plt.subplots(figsize=(10, 6))
    axis.scatter(x_train, y_train, color="blue", label=f"Training data ({len(x_train)})")
    axis.scatter(x_test, y_test, color="orange", label=f"Test data ({len(x_test)})")
    axis.plot(x_domain, y_domain, color="red", linewidth=2, label=f"Regression: y = {slope:.2f}x + {intercept:.2f}")

    axis.set_xlim(x_values.min() - 120, x_values.max() + 120)
    axis.set_ylim(min(y_values.min(), y_domain.min()) - 10, max(y_values.max(), y_domain.max()) + 10)
    axis.set_xlabel("Number")
    axis.set_ylabel("Next Number")
    axis.set_title("Linear Regression with Train/Test Split and Extended Range")
    axis.grid(True, linestyle="--", alpha=0.4)
    axis.legend()

    output_path = Path(__file__).with_name("regression_plot.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    print(f"\nSaved regression plot to {output_path}")
    print(f"Training mean absolute error: {train_error:.4f}")
    print(f"Test mean absolute error: {test_error:.4f}")
    plt.close(figure)


if __name__ == "__main__":
    main()
