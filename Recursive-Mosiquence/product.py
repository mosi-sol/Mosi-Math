import matplotlib.pyplot as plt

# Function to generate the sequence
def generate_sequence(n):
    sequence = [2, 3]
    for i in range(2, n):
        next_term = sequence[i-2] - sequence[i-1]
        sequence.append(next_term)
    return sequence

# Generate the sequence for 20 terms
n = 100 # 20
sequence = generate_sequence(n)

# Plot the sequence
x_values = list(range(n))
y_values = sequence

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b', label='Sequence Growth')

# Adding labels and title
plt.xlabel('Index (n)')
plt.ylabel('Sequence Value (a_n)')
plt.title('Sequence Growth Plot')
plt.grid(True)
plt.legend()

# Draw lines connecting each point
for i in range(1, len(x_values)):
    plt.plot([x_values[i-1], x_values[i]], [y_values[i-1], y_values[i]], 'r--')

# Show the plot
plt.show()
