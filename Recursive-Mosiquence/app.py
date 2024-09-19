def generate_sequence(n):
    # Initialize the first two terms
    sequence = [2, 3]
    
    # Generate the next terms
    for i in range(2, n):
        next_term = sequence[i-2] - sequence[i-1]
        sequence.append(next_term)
    
    return sequence

# Example usage
n = 100  # Number of terms to generate
sequence = generate_sequence(n)
print(sequence)

# [2, 3, -1, 4, -5, 9, -14, 23, -37, 60]