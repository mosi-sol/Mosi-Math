def kaprekar_constant(n):
    def kaprekar_step(num_str):
        # Sort digits in descending order
        large = int(''.join(sorted(num_str, reverse=True)))
        # Sort digits in ascending order
        small = int(''.join(sorted(num_str)))
        # Subtract the smallest number from the largest
        return large - small
    
    # Start with a random number with n digits
    num_str = str(n)
    while len(num_str) < n:
        num_str += '0'

    seen = set()
    
    while num_str not in seen:
        seen.add(num_str)
        next_num = kaprekar_step(num_str)
        num_str = str(next_num).zfill(n)
    
    return int(num_str)

# Test with 5-digit numbers
n = 4
kaprekar_5_digit = kaprekar_constant(n)
print(f"The Kaprekar constant for {n} digits is {kaprekar_5_digit}")

# Test with 5-digit numbers
n = 5
kaprekar_5_digit = kaprekar_constant(n)
print(f"The Kaprekar constant for {n} digits is {kaprekar_5_digit}")

# Test with 6-digit numbers
n = 6
kaprekar_6_digit = kaprekar_constant(n)
print(f"The Kaprekar constant for {n} digits is {kaprekar_6_digit}")
