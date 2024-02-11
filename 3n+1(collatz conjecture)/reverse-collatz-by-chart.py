# pip install pandas matplotlib networkx

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

def reverse_collatz_step(n):
    predecessors = []
    predecessors.append((n * 2, 'even'))
    if (n - 1) % 3 == 0:
        pred = (n - 1) // 3
        if pred != 1 and pred % 2 == 1:
            predecessors.append((pred, 'odd'))
    return predecessors

def find_reverse_collatz_paths(n, depth, current_path=[], all_paths=[]):
    if depth == 0 or n == 1:
        all_paths.append(current_path[::-1])
        return
    predecessors = reverse_collatz_step(n)
    if not predecessors:
        all_paths.append(current_path[::-1])
    for pred, operation in predecessors:
        find_reverse_collatz_paths(pred, depth - 1, current_path + [(pred, operation)], all_paths)
    return all_paths

def display_paths_as_table(paths):
    data = []
    for path in paths:
        for step_number, (value, operation) in enumerate(path):
            data.append({
                'Path': paths.index(path) + 1,
                'Step': step_number,
                'Value': value,
                'Operation': operation
            })
    df = pd.DataFrame(data)
    print(df)

def draw_paths_chart(paths):
    G = nx.DiGraph()
    for path in paths:
        for i in range(len(path)-1):
            G.add_edge(path[i][0], path[i+1][0])
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_size=700, with_labels=True, arrows=True)
    plt.show()

# User input
user_number = int(input("Enter a number: "))
depth = int(input("Enter the number of steps to reverse: "))

# Calculate paths
paths = find_reverse_collatz_paths(user_number, depth, current_path=[(user_number, 'start')], all_paths=[])

# Display paths as table
print("\nDisplaying paths as table:")
display_paths_as_table(paths)

# Draw paths chart
print("\nDrawing paths chart:")
draw_paths_chart(paths)
