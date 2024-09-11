def generate_division_graph(n):
    """
    Generates the division graph for the given number n.
    The graph shows where you land after multiplying by 10 and taking modulo n.
    """
    graph = {}
    for i in range(n):
        graph[i] = (i * 10) % n
    return graph

def divisibility_check(number, n):
    """
    Checks if the given number is divisible by n using the division graph method.
    Returns the remainder after division.
    """
    graph = generate_division_graph(n)
    remainder = 0
    for digit in str(number):
        remainder = graph[remainder] + int(digit)
        remainder %= n
    return remainder

def is_divisible(number, n):
    """
    Returns True if the number is divisible by n, otherwise False.
    """
    remainder = divisibility_check(number, n)
    if remainder == 0:
        print(f"{number} is divisible by {n}.")
    else:
        print(f"{number} is not divisible by {n}, remainder is {remainder}.")

# Example usage
is_divisible(3714289, 7)   # Check divisibility by 7
is_divisible(394, 13)      # Check divisibility by 13
is_divisible(987654321, 27)  # Check divisibility by 27
