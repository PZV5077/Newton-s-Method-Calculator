import tkinter as tk
import time
# ----------------------------------------------
# Help and Information Functions
# ----------------------------------------------

def show_help(root):
    help_window = tk.Toplevel(root)
    help_window.title("Help")
    help_text = (
        "This is a calculator using Newton-Raphson method \n to get the appoximate value of an equation. \n A detailed explanation of this method can be found on \n https://en.wikipedia.org/wiki/Newton's_method"
        "\n\n"
        "Usage Instructions:\n"
        "1. Enter the equation in the 'Equation' field. Use '^' for exponentiation.\n"
        "2. Enter the number of iterations in the 'Iterations' field.\n"
        "3. Enter the initial value in the 'Initial Value' field.\n"
        "4. Click 'Calculate' to perform the calculation."
    )
    tk.Label(help_window, text=help_text, font=("Microsoft YaHei UI", 12)).pack(padx=10, pady=10)

# ----------------------------------------------
# Calculation Functions
# ----------------------------------------------
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

def calculate(entry_equation, entry_iterations, entry_initial_value, label_result, label_error, log_text, command_text):
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

