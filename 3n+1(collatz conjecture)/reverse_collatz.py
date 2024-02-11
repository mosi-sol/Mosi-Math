def reverse_collatz_step(n):
    """
    Find all possible predecessors of 'n' in the Collatz sequence.
    Returns a list of tuples, each containing the predecessor and the operation applied.
    """
    predecessors = []
    
    # Even predecessor (n was n/2)
    predecessors.append((n * 2, 'even'))
    
    # Odd predecessor ((n - 1) / 3), only if n was (3n + 1)
    if (n - 1) % 3 == 0:
        pred = (n - 1) // 3
        # Ensure it's not introducing a cycle, i.e., pred should not be 1 or a result of direct 3n+1 from 1
        if pred != 1 and pred % 2 == 1:
            predecessors.append((pred, 'odd'))
    
    return predecessors

def find_reverse_collatz_paths(n, depth, current_path=[], all_paths=[]):
    """
    Recursively find and display all reverse Collatz paths for 'n' up to a given 'depth'.
    Each path is a list of steps showing how 'n' could have been reached.
    """
    if depth == 0 or n == 1:
        # Reverse the path to show it from the origin to the final number
        all_paths.append(current_path[::-1])
        return
    
    predecessors = reverse_collatz_step(n)
    if not predecessors:
        all_paths.append(current_path[::-1])
    
    for pred, operation in predecessors:
        find_reverse_collatz_paths(pred, depth - 1, current_path + [(pred, operation)], all_paths)
    
    return all_paths

# User input for number and depth
user_number = int(input("Enter a number: "))
depth = int(input("Enter the number of steps to reverse: "))

# Calculate paths
paths = find_reverse_collatz_paths(user_number, depth, current_path=[(user_number, 'start')], all_paths=[])

# Display paths
print(f"\nAll possible reverse Collatz paths for {user_number} over {depth} steps:")
for path in paths:
    print(" | ".join(f"{step[0]} ({step[1]})" for step in path))
