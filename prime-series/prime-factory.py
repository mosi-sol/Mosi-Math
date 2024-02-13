# mosi said: this is the proof of behiverial morality of small numbers :)
# relation of "Faulhaber's Fabulous Formula (and Bernoulli Numbers)" to the prime numbers

import tkinter as tk
from tkinter import ttk, filedialog, messagebox

def sieve_of_eratosthenes(start, end):
    prime = [True for _ in range(end+1)]
    prime[0], prime[1] = False, False
    for p in range(2, int(end**0.5) + 1):
        if prime[p]:
            for i in range(p*p, end+1, p):
                prime[i] = False
    return [p for p in range(start, end+1) if prime[p]]

def find_primes():
    try:
        start = int(start_entry.get())
        end = int(end_entry.get())
        if start > end or start < 0:
            messagebox.showerror("Error", "Invalid range. Please enter a valid start and end range.")
            return
        primes = sieve_of_eratosthenes(start, end)
        # Clear the treeview content before inserting new results
        for i in tree.get_children():
            tree.delete(i)
        # Inserting new results
        for i, prime in enumerate(primes):
            tree.insert('', 'end', values=(i+1, prime))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integer values for start and end range.")

def save_results():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            for child in tree.get_children():
                index, prime = tree.item(child)["values"]
                file.write(f"{index}. {prime}\n")
        messagebox.showinfo("Success", "The prime numbers have been saved successfully.")

# Create the main window
root = tk.Tk()
root.title("Prime Number Finder")

# Input fields for start and end range
range_frame = tk.Frame(root)
range_frame.pack(pady=10)

tk.Label(range_frame, text="Start:").pack(side=tk.LEFT)
start_entry = tk.Entry(range_frame, width=10)
start_entry.pack(side=tk.LEFT, padx=5)

tk.Label(range_frame, text="End:").pack(side=tk.LEFT)
end_entry = tk.Entry(range_frame, width=10)
end_entry.pack(side=tk.LEFT, padx=5)

# Find button
find_button = tk.Button(root, text="Find Primes", command=find_primes)
find_button.pack(pady=5)

# Frame for the treeview and scrollbar
tree_frame = tk.Frame(root)
tree_frame.pack()

tree_scroll = tk.Scrollbar(tree_frame)
tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

tree = ttk.Treeview(tree_frame, columns=('Index', 'Prime Number'), show="headings", yscrollcommand=tree_scroll.set)
tree.heading('Index', text='Index')
tree.heading('Prime Number', text='Prime Number')

tree.pack(side=tk.LEFT)
tree_scroll.config(command=tree.yview)

# Save button
save_button = tk.Button(root, text="Save Results", command=save_results)
save_button.pack(pady=5)

root.mainloop()
