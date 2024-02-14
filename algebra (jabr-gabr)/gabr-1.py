import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp

# Create the main window
root = tk.Tk()
root.title("Algebraic Equation Visualizer")

# Function to plot the equation
def plot_equation():
    equation_input = equation.get()
    try:
        # Parse the equation
        x = sp.symbols('x')
        equation_parsed = sp.sympify(equation_input)

        # Generate x values
        x_vals = np.linspace(-10, 10, 400)
        # Generate y values based on the equation
        y_vals = [equation_parsed.subs(x, val).evalf() for val in x_vals]

        # Clear previous figure
        plt.clf()

        # Create a new figure and plot the equation
        fig = plt.figure(figsize=(6, 4))
        plt.plot(x_vals, y_vals, label=f'y = {equation_input}')
        plt.axhline(0, color='black', lw=2)
        plt.axvline(0, color='black', lw=2)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Graph of the Equation')
        plt.legend()
        plt.grid(True)

        # Embed the plot into the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=2, column=0, columnspan=4)
        canvas.draw()

    except Exception as e:
        tk.messagebox.showerror("Error", "Invalid equation. Please enter a valid algebraic equation.")

# Create a text entry to input the equation
equation = tk.StringVar()
entry_box = ttk.Entry(root, textvariable=equation, font=('Arial', 12), width=50)
entry_box.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

# Create a "Plot" button
plot_button = ttk.Button(root, text="Plot Equation", command=plot_equation)
plot_button.grid(row=0, column=3, pady=10, padx=10)

root.mainloop()
