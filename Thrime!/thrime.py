import math
import matplotlib.pyplot as plt

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Function to generate even numbers that don't end in 6
def even_numbers_exclude_6(limit):
    even_nums = []
    for num in range(2, limit + 1, 2):  # Start from 2, increment by 2 (even numbers)
        if num % 10 != 6:  # Exclude numbers ending in 6
            even_nums.append(num)
    return even_nums

# Function to create logarithmic sequence and check primes
def find_prime_logarithmic(limit):
    even_nums = even_numbers_exclude_6(limit)
    primes = []
    non_primes = []
    x_values = []
    y_values = []
    
    for i in range(len(even_nums)):
        # Use a logarithmic step to select the next even number
        step = int(math.log2(i + 2))  # Logarithmic progression
        if i + step < len(even_nums):
            even_num = even_nums[i + step]
            candidate_sum = 3 + even_num
            x_values.append(even_num)  # Track x (even number)
            y_values.append(candidate_sum)  # Track y (sum 3 + even number)
            if is_prime(candidate_sum):
                primes.append(candidate_sum)
            else:
                non_primes.append(candidate_sum)
    
    return primes, non_primes, x_values, y_values

# Plotting the results
def plot_distribution(primes, non_primes, x_values, y_values):
    # Create a scatter plot with different colors for primes and non-primes
    plt.figure(figsize=(10, 6))

    # Plot all numbers as non-primes initially
    plt.scatter(x_values, y_values, color='red', label='Non-Prime Sums', alpha=0.5)

    # Highlight prime numbers in green
    prime_y_values = [y for y in y_values if y in primes]
    prime_x_values = [x for x, y in zip(x_values, y_values) if y in primes]
    plt.scatter(prime_x_values, prime_y_values, color='green', label='Prime Sums', alpha=0.7)

    # Add labels and title
    plt.title('Distribution of Prime and Non-Prime Sums', fontsize=16)
    plt.xlabel('Even Number', fontsize=14)
    plt.ylabel('Sum (3 + Even Number)', fontsize=14)
    plt.legend()
    plt.grid(True)
    plt.show()

# Define the limit for even numbers to check
limit = 1000
primes, non_primes, x_values, y_values = find_prime_logarithmic(limit)

print(f"Prime numbers found: {primes}")
print(f"Non-Prime numbers found: {non_primes}")

# Plot the distribution of primes and non-primes
plot_distribution(primes, non_primes, x_values, y_values)
