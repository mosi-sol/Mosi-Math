import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

# Logistic map function
def logistic_map(r, x0, iterations):
    x_values = [x0]
    x = x0
    for _ in range(iterations):
        x = r * x * (1 - x)
        x_values.append(x)
    return x_values

# Function to update plot and table
def update():
    try:
        r = float(entry_r.get())
        x0 = float(entry_x0.get())
        iterations = int(entry_iterations.get())
        x_values = logistic_map(r, x0, iterations)
        
        # Update plot
        ax.clear()
        ax.plot(x_values, '-o', markersize=3)
        ax.set_title("Logistic Map Simulation")
        ax.set_xlabel("Iteration")
        ax.set_ylabel("x Value")
        canvas.draw()
        
        # Update table
        for widget in frame_table.winfo_children():
            widget.destroy()
        pd.DataFrame(x_values, columns=['x Value']).to_csv('logistic_map_values.csv', index_label='Iteration')
        table = ttk.Treeview(frame_table)
        table["columns"] = ("Iteration", "x Value")
        table.column("#0", width=0, stretch=tk.NO)
        table.column("Iteration", anchor=tk.CENTER, width=80)
        table.column("x Value", anchor=tk.CENTER, width=100)
        
        table.heading("#0", text="", anchor=tk.CENTER)
        table.heading("Iteration", text="Iteration", anchor=tk.CENTER)
        table.heading("x Value", text="x Value", anchor=tk.CENTER)
        
        for i, value in enumerate(x_values):
            table.insert(parent='', index='end', iid=i, text='', values=(i, value))
        table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(frame_table, orient=tk.VERTICAL, command=table.yview)
        table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    except ValueError:
        print("Please enter valid numbers.")

# Main window
root = tk.Tk()
root.title("Logistic Map Visualizer")
root.geometry("800x600")

# Input frame
frame_input = ttk.Frame(root)
frame_input.pack(padx=10, pady=5, fill=tk.X)

label_r = ttk.Label(frame_input, text="r:")
label_r.pack(side=tk.LEFT, padx=(0, 5))
entry_r = ttk.Entry(frame_input)
entry_r.insert(0, "3.9")
entry_r.pack(side=tk.LEFT, padx=(0, 10))

label_x0 = ttk.Label(frame_input, text="x0:")
label_x0.pack(side=tk.LEFT, padx=(0, 5))
entry_x0 = ttk.Entry(frame_input)
entry_x0.insert(0, "0.5")
entry_x0.pack(side=tk.LEFT, padx=(0, 10))

label_iterations = ttk.Label(frame_input, text="Iterations:")
label_iterations.pack(side=tk.LEFT, padx=(0, 5))
entry_iterations = ttk.Entry(frame_input)
entry_iterations.insert(0, "100")
entry_iterations.pack(side=tk.LEFT, padx=(0, 10))

button_update = ttk.Button(frame_input, text="Update", command=update)
button_update.pack(side=tk.LEFT, padx=(10, 0))

# Plot frame
frame_plot = ttk.Frame(root)
frame_plot.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

fig, ax = plt.subplots(figsize=(5, 4))
canvas = FigureCanvasTkAgg(fig, master=frame_plot)
widget = canvas.get_tk_widget()
widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Table frame
frame_table = ttk.Frame(root)
frame_table.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

root.mainloop()
