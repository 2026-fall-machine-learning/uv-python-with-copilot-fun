# uv Python With Copilot Fun

A tiny Python project managed with [uv](https://docs.astral.sh/uv/) that prints
ASCII-art names using [`pyfiglet`](https://pypi.org/project/pyfiglet/) and
demonstrates a small linear regression with
[`pandas`](https://pandas.pydata.org/) and
[`matplotlib`](https://matplotlib.org/).

## Getting started after cloning

Install uv using the
[official installation instructions](https://docs.astral.sh/uv/getting-started/installation/).
Then open PowerShell in the cloned project directory.

Check which Python versions uv currently knows about before changing anything:

```powershell
uv python list
```

This project intentionally targets Python `3.9.25`. If it is not listed as
installed, install it with uv:

```powershell
uv python install 3.9.25
```

Create the project virtual environment with that interpreter:

```powershell
uv venv --python 3.9.25
```

Activate the environment in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the project and its dependencies:

```powershell
uv sync
```

Run the greeting:

```powershell
uv run main.py
```

The script first prints the ASCII-art names, then reads `counting-data.csv`.
It treats `Number` as the input column and `NextNumber` as the output column,
prints the fitted linear equation, and saves the chart to
`linear-regression.png`. The regression calculation is done directly with
pandas operations; scikit-learn is not required for this simple example. When
run locally, the script also opens the chart in a plot window after saving it.

Inspect the available Python versions again and compare the result with the
earlier command:

```powershell
uv python list
```

With the virtual environment active, inspect its installed packages:

```powershell
uv pip list
```

To avoid activating the environment, point uv directly at its interpreter:

```powershell
uv pip list --python .\.venv\Scripts\python.exe
```
