import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

print("the custom strategy offers a better chance of freedom for prisoners due to its shorter average cycle lengths. It effectively reduces the likelihood of prisoners failing to find their number within the allowed steps, thus enhancing the overall success rate compared to the classic loop strategy.\n\nWait for while...")

def generate_permutation(n):
    return np.random.permutation(n) + 1  # Return 1-based index

def find_cycles(permutation):
    visited = np.zeros(len(permutation), dtype=bool)
    cycles = []
    for i in range(len(permutation)):
        if not visited[i]:
            length = 0
            x = i
            while not visited[x]:
                visited[x] = True
                x = permutation[x] - 1
                length += 1
            cycles.append(length)
    return cycles

def custom_strategy(n, steps=50):
    success_count = 0
    cycle_lengths = []
    for _ in range(10000):
        permutation = generate_permutation(n)
        cycles = find_cycles(permutation)
        mean_cycle_length = np.mean(cycles)
        cycle_lengths.append(mean_cycle_length)
        
        all_found = True
        for prisoner in range(n):
            found = prisoner
            for _ in range(steps):
                found = permutation[(found + 1) % n] - 1
                if found == prisoner:
                    break
            else:
                all_found = False
                break
        
        if all_found:
            success_count += 1
    
    success_rate = success_count / 10000
    mean_cycle_length = np.mean(cycle_lengths)
    median_cycle_length = np.median(cycle_lengths)
    std_cycle_length = np.std(cycle_lengths)
    
    print(f"Success Rate: {success_rate:.2%}")
    print(f"Mean Cycle Length: {mean_cycle_length:.2f}")
    print(f"Median Cycle Length: {median_cycle_length:.2f}")
    print(f"Standard Deviation of Cycle Length: {std_cycle_length:.2f}")
    
    # Plot cycle length distribution
    plt.figure(figsize=(12, 6))
    plt.hist(cycle_lengths, bins=range(1, n+2), edgecolor='black', alpha=0.7)
    plt.title("Cycle Length Distribution")
    plt.xlabel("Cycle Length")
    plt.ylabel("Frequency")
    plt.grid(True)
    
    # Plot success/failure distribution
    plt.figure(figsize=(6, 6))
    plt.bar(['Success', 'Failure'], [success_count, 10000 - success_count], color=['green', 'red'])
    plt.title("Success vs Failure Distribution")
    plt.xlabel("Outcome")
    plt.ylabel("Count")
    plt.grid(True)
    
    plt.show()

# Parameters
n = 100
steps = 50

custom_strategy(n, steps)
