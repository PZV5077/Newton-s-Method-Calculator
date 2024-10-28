import tkinter as tk
from tkinter import ttk
import re
import time

def show_help():
    help_window = tk.Toplevel(root)
    help_window.title("Help")
    help_text = (
        "This is a calculator using Newton-Raphson method \n to get the appoximate value of an equation. \n A detiled explaination of this methord can be found on \n https://en.wikipedia.org/wiki/Newton's_method"
        "\n\n"
        "Usage Instructions:\n"
        "1. Enter the equation in the 'Equation' field. Use '^' for exponentiation.\n"
        "2. Enter the number of iterations in the 'Iterations' field.\n"
        "3. Enter the initial value in the 'Initial Value' field.\n"
        "4. Click 'Calculate' to perform the calculation.\n\n"
        "\n"
        "Powered by Eric Zhang and Levi Ji, \n as a course work of Computer Informatic System 12, \n in October 2024. "
    )
    tk.Label(help_window, text=help_text, font=("Microsoft YaHei UI", 12)).pack(padx=10, pady=10)


def evaluate_function(func, x):
    return eval(func)

def derivative(func, x, h=1e-5):
    return (evaluate_function(func, x + h) - evaluate_function(func, x - h)) / (2 * h)

def newton_method(func, x0, iterations):
    log = []
    for i in range(iterations):
        f_x0 = evaluate_function(func, x0)
        f_prime_x0 = derivative(func, x0)
        if f_prime_x0 == 0:
            log.append(f"Iteration {i}: Derivative is zero, stopping calculation.")
            return None, None, log  # Avoid division by zero
        x0 = x0 - f_x0 / f_prime_x0
        log.append(f"Iteration {i}: x = {x0}, f(x) = {f_x0}, f'(x) = {f_prime_x0}")
    return x0, abs(f_x0), log

def calculate():
    equation = entry_equation.get().replace('^', '**')
    if '=' in equation:
        left_side, right_side = equation.split('=')
        equation = f"({left_side}) - ({right_side})"
    iterations = int(entry_iterations.get())
    x0 = float(entry_initial_value.get())
    result, error, log = newton_method(equation, x0, iterations)
    if result is not None:
        label_result.config(text=f"Result: {result}")
        label_error.config(text=f"Error: {error}")
    else:
        label_result.config(text="Result: Error during calculation")
        label_error.config(text="Error: Unable to calculate")
    
    # Display log
    log_text.delete(1.0, tk.END)
    for entry in log:
        log_text.insert(tk.END, entry + "\n")
    
    
    
    # Display commands
    start_time = time.time()
    command_text.delete(1.0, tk.END)
    command_text.insert(tk.END, f"Executing Newton's Method with {iterations} iterations\n")
    command_text.insert(tk.END, f"Initial value: {x0}\n")
    command_text.insert(tk.END, f"Equation: {equation}\n")
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    command_text.insert(tk.END, f"Calculation time: {elapsed_time:.6f} seconds\n")


# Create main window
root = tk.Tk()
root.title("  Magical Calculator")

# Get screen width and set window width to 1/4 of the screen width
screen_width = root.winfo_screenwidth()
window_width = screen_width // 4
root.geometry(f"{window_width*3}x400")  # Increase window width

# Set default font
default_font = ("Microsoft YaHei UI", 12)

# Create and place title with Help button
title_font = ("Microsoft YaHei UI", 24, "bold")
title_frame = tk.Frame(root)
title_frame.pack(fill=tk.X, padx=10, pady=10)

title_label = tk.Label(title_frame, text="Magical Calculator", font=title_font)
title_label.pack(side=tk.LEFT, expand=True)

help_button = tk.Button(title_frame, text="Help", font=default_font, command=show_help)
help_button.pack(side=tk.RIGHT)

# Create and place components in left frame
left_frame = tk.Frame(root)
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

button_calculate = tk.Button(left_frame, text="Calculate", command=calculate, font=default_font)
button_calculate.pack(pady=5)

label_result = tk.Label(left_frame, text="Result: ", font=default_font)
label_result.pack(pady=5)

label_error = tk.Label(left_frame, text="Error: ", font=default_font)
label_error.pack(pady=5)

# Create notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=10, pady=10)

# Create Calculation Log tab
log_frame = tk.Frame(notebook)
log_text = tk.Text(log_frame, font=default_font, height=15, width=100)
log_text.pack(pady=5)
notebook.add(log_frame, text="Calculation Log")

# Create Command Execution tab
command_frame = tk.Frame(notebook)
command_text = tk.Text(command_frame, font=default_font, height=15, width=100)
command_text.pack(pady=5)
notebook.add(command_frame, text="Command Execution")

# Run main loop
root.mainloop()