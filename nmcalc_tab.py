import tkinter as tk
from tkinter import ttk
from nmfunc import show_help, calculate

def create_nmcalculator_tab(notebook, default_font):
    # Create first tab for the calculator
    calculator_frame = tk.Frame(notebook)
    notebook.add(calculator_frame, text="Newton`s Method")

    # Create and place title with Help button in the calculator tab
    title_font = ("Microsoft YaHei UI", 24, "bold")
    title_frame = tk.Frame(calculator_frame)
    title_frame.pack(fill=tk.X, padx=10, pady=10)

    title_label = tk.Label(title_frame, text="Newton-Raphson Method Calculator", font=title_font)
    title_label.pack(side=tk.LEFT, expand=True)

    help_button = tk.Button(title_frame, text="Help", font=default_font, command=lambda: show_help(calculator_frame))
    help_button.pack(side=tk.RIGHT)

    # Create and place components in left frame in the calculator tab
    left_frame = tk.Frame(calculator_frame)
    left_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10, pady=10)

    tk.Label(left_frame, text="Equation:", font=default_font).pack(pady=5)
    entry_equation = tk.Entry(left_frame, font=default_font)
    entry_equation.pack(pady=5)

    tk.Label(left_frame, text="Iterations:", font=default_font).pack(pady=5)
    entry_iterations = tk.Entry(left_frame, font=default_font)
    entry_iterations.pack(pady=5)

    tk.Label(left_frame, text="Initial Value:", font=default_font).pack(pady=5)
    entry_initial_value = tk.Entry(left_frame, font=default_font)
    entry_initial_value.pack(pady=5)

    button_calculate = tk.Button(left_frame, text="Calculate", command=lambda: calculate(entry_equation, entry_iterations, entry_initial_value, label_result, label_error, log_text, command_text), font=default_font)
    button_calculate.pack(pady=5)

    label_result = tk.Label(left_frame, text="Result: ", font=default_font)
    label_result.pack(pady=5)

    label_error = tk.Label(left_frame, text="Error: ", font=default_font)
    label_error.pack(pady=5)

    # Create notebook for tabs within the calculator tab
    inner_notebook = ttk.Notebook(calculator_frame)
    inner_notebook.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Create Calculation Log tab
    log_frame = tk.Frame(inner_notebook)
    log_text = tk.Text(log_frame, font=default_font, height=15, width=100)
    log_text.pack(pady=5)
    inner_notebook.add(log_frame, text="Calculation Log")

    # Create Command Execution tab
    command_frame = tk.Frame(inner_notebook)
    command_text = tk.Text(command_frame, font=default_font, height=15, width=100)
    command_text.pack(pady=5)
    inner_notebook.add(command_frame, text="Command Execution")

    return calculator_frame