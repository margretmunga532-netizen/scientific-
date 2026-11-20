# BIT 2118 Scientific Computing — Group Work (Tasks A–S)

This project reproduces the folder layout shown in the supplied File Explorer screenshot.

## Project structure

```text
bit2118-scientific-computing/
├── code/
│   ├── task_02_numpy_arrays.py
│   ├── task_03_vectorization.py
│   ├── task_04_floating_point_errors.py
│   ├── task_05_matrix_algebra.py
│   ├── task_06_linear_systems.py
│   ├── task_07_gaussian_elimination_lu.py
│   ├── task_08_iterative_methods.py
│   ├── task_09_eigenvalues.py
│   ├── task_10_bisection_fixed_point.py
│   ├── task_11_newton_secant.py
│   ├── task_12_nonlinear_equations.py
│   ├── task_13_interpolation.py
│   ├── task_14_curve_fitting.py
│   ├── task_15_numerical_differentiation.py
│   ├── task_16_numerical_integration.py
│   ├── task_17_euler_method.py
│   ├── task_18_scipy_ode_solver.py
│   ├── task_19_optimization.py
│   └── task_20_monte_carlo.py
├── docs/
│   └── BIT2118_Group_Work_Tasks_A-S.docx
├── .gitignore
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.10 or newer
- NumPy
- SciPy
- Matplotlib

Install dependencies from this directory:

```bash
python -m pip install -r requirements.txt
```

## Running a task

Run commands from the project root. For example:

```bash
python code/task_02_numpy_arrays.py
python code/task_18_scipy_ode_solver.py
```

Some tasks display plots using Matplotlib. Close the plot window to allow the script to finish.

## Source and scope

The scripts contain the modified real-world case code for Tasks 2–20, transcribed from the supplied group-work document. The original Word document is retained in `docs/` for reference. Task labels A–S correspond to Tasks 2–20 in the source document.

If a code listing in the Word document contains a formatting or transcription issue, compare it with the source document before making changes; the scripts are intentionally based on that document rather than silently changing its numerical assumptions or results.
