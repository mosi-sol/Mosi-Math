import tkinter as tk
from tkinter import ttk, scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range(x, y):
    primes = []
    for number in range(x, y + 1):
        if is_prime(number):
            primes.append(number)
    return primes

def on_submit():
    x = int(x_entry.get())
    y = int(y_entry.get())
    primes = find_primes_in_range(x, y)
    
    # Display primes
    result_area.delete('1.0', tk.END)
    result_area.insert(tk.INSERT, f"Prime numbers between {x} and {y}:\n{primes}\n")
    
    # Prime distribution plot
    fig.clear()
    ax = fig.add_subplot(111)
    ax.hist(primes, bins=10, color='skyblue')
    ax.set_title('Prime Distribution')
    canvas.draw()

    # Gap between consecutive primes plot
    prime_diffs = [primes[i] - primes[i-1] for i in range(1, len(primes))]
    fig2.clear()
    ax2 = fig2.add_subplot(111)
    ax2.plot(primes[1:], prime_diffs, marker='o', linestyle='-')
    ax2.set_title('Gap Between Consecutive Primes')
    canvas2.draw()

app = tk.Tk()
app.title('Prime Number Application')
app.geometry("600x800")

# Create a main canvas with scrollbars
main_canvas = tk.Canvas(app)
main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

scrollbar = ttk.Scrollbar(app, orient=tk.VERTICAL, command=main_canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

main_canvas.configure(yscrollcommand=scrollbar.set)
main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))

# Create a frame inside the canvas
main_frame = tk.Frame(main_canvas)

# Add that new frame to a window in the canvas
main_canvas.create_window((0,0), window=main_frame, anchor="nw")

# Now, add your UI elements to the main_frame instead of app
x_label = tk.Label(main_frame, text="Enter X:")
x_label.pack()
x_entry = tk.Entry(main_frame)
x_entry.pack()

y_label = tk.Label(main_frame, text="Enter Y:")
y_label.pack()
y_entry = tk.Entry(main_frame)
y_entry.pack()

submit_btn = tk.Button(main_frame, text="Find Primes", command=on_submit)
submit_btn.pack()

result_area = scrolledtext.ScrolledText(main_frame, width=40, height=10)
result_area.pack()

# Prime distribution plot
fig = plt.Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=main_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Gap between consecutive primes plot
fig2 = plt.Figure(figsize=(5, 4), dpi=100)
canvas2 = FigureCanvasTkAgg(fig2, master=main_frame)
canvas2_widget = canvas2.get_tk_widget()
canvas2_widget.pack()

app.mainloop()
