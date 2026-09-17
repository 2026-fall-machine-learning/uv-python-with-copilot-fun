from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyfiglet

CSV_PATH = Path(__file__).parent / "2026-fall-ml-week-04-mon.csv"
TRAIN_FRACTION = 0.7  # poor man's train/test split: fit only on this share of rows
RANDOM_SEED = 42  # fixed seed so the split stays reproducible as you edit the CSV
EXTRAPOLATE_MARGIN = 100  # extend the fit line this far past the data's min/max x


def plot_linear_regression(csv_path: Path = CSV_PATH) -> None:
    """Fit a simple linear regression on a train split, plot train/test points, and
    extend the fit line 100 units past the data's min/max x for extrapolation."""
    df = pd.read_csv(csv_path)

    # Poor man's train/test split: shuffle row indices with a fixed seed, then slice.
    rng = np.random.default_rng(RANDOM_SEED)
    indices = rng.permutation(len(df))
    split_at = max(1, min(len(df) - 1, round(len(df) * TRAIN_FRACTION))) if len(df) > 1 else len(df)
    train_idx, test_idx = indices[:split_at], indices[split_at:]

    train_df, test_df = df.iloc[train_idx], df.iloc[test_idx]
    x_train, y_train = train_df["Number"], train_df["NextNumber"]

    # np.polyfit(x, y, 1) fits a degree-1 (straight line) polynomial: y = slope * x + intercept
    slope, intercept = np.polyfit(x_train, y_train, 1)

    # Extend the fit line 100 past the min/max of ALL x values (train + test).
    x_all = df["Number"]
    line_x = np.linspace(x_all.min() - EXTRAPOLATE_MARGIN, x_all.max() + EXTRAPOLATE_MARGIN, 200)
    line_y = slope * line_x + intercept

    plt.scatter(x_train, y_train, color="tab:blue", label="Train")
    if len(test_df):
        plt.scatter(test_df["Number"], test_df["NextNumber"], color="tab:orange", label="Test")
    plt.plot(line_x, line_y, color="red", label=f"Fit (train): y = {slope:.2f}x + {intercept:.2f}")
    plt.xlabel("Number")
    plt.ylabel("NextNumber")
    plt.title("Linear Regression Fit (train/test split, extrapolated \u00b1100)")
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
