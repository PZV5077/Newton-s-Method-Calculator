import tkinter as tk
from tkinter import ttk
from nmcalc_tab import create_nmcalculator_tab


# Create main window
root = tk.Tk()
root.title("Student`s Calculator")
root.resizable(False, False)
root.iconphoto(False, tk.PhotoImage(file="icon.png"))

# Get screen width and set window width to 1/4 of the screen width
screen_width = root.winfo_screenwidth()
window_width = screen_width // 4
root.geometry(f"{window_width*3}x500")  # Set window width and height

# Set default font
default_font = ("Microsoft YaHei UI", 12)

# Create notebook for tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill=tk.BOTH)

# Create calculator tab
create_nmcalculator_tab(notebook, default_font)

# Run main loop
root.mainloop()