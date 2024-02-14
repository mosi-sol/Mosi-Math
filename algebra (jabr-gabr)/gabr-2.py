# M zoo (NWNM)= (2*sin(x)) * cos(x)
# M zoo = -(1/2) * sin(2*x) + cos(y)
# M zoo = cos(y - (x - 2) * x-y) / 3
# M zoo = sin(y - (x - 2) * x-y) / 3
# M zoo = (cos(y - (x - 2) * x-y) / 3 ) - (sin(y - (x - 2) * x-y) / 3)

# roof tail = sin(x) -  cos(x) - y

# bear market = (sin(y) +  cos(y) ) * y

# mandala = sin(x*y)
# mandala = cos(x*y)* log(x-y)

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Create the main window
root = tk.Tk()
root.title("Algebraic Equation Visualizer")

# Function to plot the equation based on the selected mode (2D or 3D)
def plot_equation():
    equation_input = equation.get()
    plot_mode = plot_mode_var.get()
    
    if plot_mode == '2D':
        plot_2d_equation(equation_input)
    elif plot_mode == '3D':
        plot_3d_equation(equation_input)
    else:
        messagebox.showerror("Error", "Please select a valid plot mode.")

# Function to plot 2D equations
def plot_2d_equation(equation_input):
    try:
        x = sp.symbols('x')
        # Parse the equation
        equation_parsed = sp.sympify(equation_input)

        # Generate x values
        x_vals = np.linspace(-10, 10, 400)
        # Generate y values based on the equation
        y_vals = [equation_parsed.subs(x, val) for val in x_vals]

        # Plotting
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=equation_input)
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)
        ax.legend()
        ax.grid(True)

        # Embed the plot into the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=root) 
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=3, columnspan=4)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to plot 3D equations
def plot_3d_equation(equation_input):
    try:
        x, y = sp.symbols('x y')
        # Parsing the equation assuming z as a function of x and y
        equation_parsed = sp.sympify(equation_input)

        # Generate x, y values
        x_vals = np.linspace(-10, 10, 100)
        y_vals = np.linspace(-10, 10, 100)
        x_vals, y_vals = np.meshgrid(x_vals, y_vals)
        z_vals = sp.lambdify((x, y), equation_parsed, 'numpy')(x_vals, y_vals)

        # Plotting
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x_vals, y_vals, z_vals, cmap='viridis')

        # Embed the plot into the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=3, columnspan=4)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# UI Components
equation = tk.StringVar()
entry_box = ttk.Entry(root, textvariable=equation, width=50)
entry_box.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

plot_mode_var = tk.StringVar(value='2D')
ttk.Radiobutton(root, text='2D', variable=plot_mode_var, value='2D').grid(row=1, column=0)
ttk.Radiobutton(root, text='3D', variable=plot_mode_var, value='3D').grid(row=1, column=1)

plot_button = ttk.Button(root, text="Plot Equation", command=plot_equation)
plot_button.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
