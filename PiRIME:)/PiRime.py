# pi prime generator, mosi pirime :)

import math

def is_prime(n):
    # Check if n is a prime number. n is expected to be an integer.
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes_in_range_with_pi_checks(x, y):
    # Find all prime numbers between x and y, inclusive, and perform pi-related checks.
    primes = []
    for number in range(x, y + 1):
        if is_prime(number):
            # Multiplying by π and rounding
            number_multiplied_by_pi = number * math.pi
            rounded_down = math.floor(number_multiplied_by_pi)
            rounded_up = math.ceil(number_multiplied_by_pi)

            # Check if rounded values are prime
            is_rounded_down_prime = is_prime(rounded_down)
            is_rounded_up_prime = is_prime(rounded_up)

            # Append results if any rounded value is prime
            if is_rounded_down_prime or is_rounded_up_prime:
                primes.append({
                    'prime': number,
                    'multiplied_by_pi_rounded_down': rounded_down,
                    'is_rounded_down_prime': is_rounded_down_prime,
                    'multiplied_by_pi_rounded_up': rounded_up,
                    'is_rounded_up_prime': is_rounded_up_prime,
                })
    return primes

# Given values
x = 1000
y = 1500

# Find and selectively print prime numbers between x and y with π multiplication and rounding checks
prime_numbers_with_checks = find_primes_in_range_with_pi_checks(x, y)
for item in prime_numbers_with_checks:
    if item['is_rounded_down_prime']:
        print(f"Prime number {item['prime']} when multiplied by π and rounded down to {item['multiplied_by_pi_rounded_down']} is prime: {item['is_rounded_down_prime']}")
    if item['is_rounded_up_prime']:
        print(f"Prime number {item['prime']} when multiplied by π and rounded up to {item['multiplied_by_pi_rounded_up']} is prime: {item['is_rounded_up_prime']}")
