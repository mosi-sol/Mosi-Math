import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

def reverse_collatz_step(n):
    predecessors = []
    # Direct reverse step: n*2 for even
    predecessors.append((n * 2, 'even'))
    # Reverse step for odd, ensuring it results in an odd number
    if (n - 1) % 3 == 0 and ((n - 1) // 3) % 2 == 1 and (n - 1) // 3 != 1:
        predecessors.append(((n - 1) // 3, 'odd'))
    return predecessors

def find_reverse_collatz_paths(n, depth, current_path=[], all_paths=[]):
    if depth == 0:
        all_paths.append(current_path[::-1])
        return
    predecessors = reverse_collatz_step(n)
    for pred, operation in predecessors:
        find_reverse_collatz_paths(pred, depth - 1, current_path + [(n, operation)], all_paths)
    return all_paths

def display_paths_as_table(paths):
    data = []
    for path_index, path in enumerate(paths):
        for step_number, (value, operation) in enumerate(path):
            data.append({'Path': path_index + 1, 'Step': step_number, 'Value': value, 'Operation': operation})
    df = pd.DataFrame(data)
    print(df)

def draw_paths_chart(paths):
    G = nx.DiGraph()
    for path in paths:
        for i in range(len(path) - 1):
            G.add_edge(path[i + 1][0], path[i][0])  # Reverse direction for correct visualization
    pos = nx.spring_layout(G, seed=42)  # Seed for reproducible layout
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", font_size=8)
    plt.title("Reverse Collatz Paths")
    plt.show()

def count_number_groups_and_draw_chart(paths):
    number_counts = {}
    for path in paths:
        for value, _ in path:
            if value in number_counts:
                number_counts[value] += 1
            else:
                number_counts[value] = 1
    numbers = list(number_counts.keys())
    counts = list(number_counts.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(numbers, counts, color='skyblue')
    plt.xlabel('Number')
    plt.ylabel('Count')
    plt.title('Frequency of Numbers in Reverse Collatz Paths')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

# Main execution
user_number = int(input("Enter a number: "))
depth = int(input("Enter the number of steps to reverse: "))

paths = find_reverse_collatz_paths(user_number, depth, current_path=[], all_paths=[])

print("\nPaths as Table:")
display_paths_as_table(paths)

print("\nDrawing Reverse Collatz Paths:")
draw_paths_chart(paths)

print("\nDrawing Number Group Frequencies:")
count_number_groups_and_draw_chart(paths)
