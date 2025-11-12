import sys
import math

# A helper function to create a non-trivial starting number (like 4321 for N=4, or 54321 for N=5)
def get_starting_number(n):
    """Generates a starting number with n distinct digits (e.g., 4321 for n=4)."""
    if n > 9:
        # The routine generally works best for 3, 4, 5, 6, 7, 8 digits.
        # Generating a unique number with more than 9 digits is complex.
        return 1
    
    # Use descending distinct digits for a good starting point
    digits = [str(i) for i in range(n, 0, -1)]
    return int("".join(digits))

def kaprekar_step(num_str, digit_count):
    """
    Performs one step of the Kaprekar routine:
    1. Sort digits to get the largest number (large).
    2. Sort digits to get the smallest number (small).
    3. Calculate large - small.
    4. Pad the result with leading zeros back to digit_count.
    """
    # Sort digits in descending order for the largest number
    large = int(''.join(sorted(num_str, reverse=True)))
    
    # Sort digits in ascending order for the smallest number
    small = int(''.join(sorted(num_str)))
    
    # Subtract the smallest number from the largest
    result = large - small
    
    # Pad the result back to the required number of digits (e.g., 999 -> 0999 for 4-digits)
    return str(result).zfill(digit_count)

def find_kaprekar_result(digit_count, initial_number):
    """
    Runs the Kaprekar routine until it finds the constant or enters a cycle.
    
    Args:
        digit_count (int): The number of digits (N).
        initial_number (int): The starting number to test.
        
    Returns:
        str: The resulting constant or the first number of the cycle.
    """
    
    num_str = str(initial_number).zfill(digit_count)
    seen = {}  # Store seen numbers and the step they appeared at
    step = 0
    
    # Check for the invalid all-same-digit number (e.g., 111, 4444)
    if len(set(num_str)) == 1:
        return f"Start: {num_str}. Result: 0. Invalid starting number (all digits are the same)."
        
    print(f"\n--- Starting Kaprekar routine with {num_str} ({digit_count} digits) ---")

    # Limit steps in case of non-convergence (shouldn't happen with the routine, but for safety)
    MAX_STEPS = 20

    while num_str not in seen and step < MAX_STEPS:
        seen[num_str] = step
        print(f"Step {step}: {num_str}")
        
        # Calculate the next number
        next_num_str = kaprekar_step(num_str, digit_count)
        
        # Check for the constant (if next_num_str is the same as the current num_str)
        if next_num_str == num_str:
             return f"Start: {initial_number}. Result: The constant is {next_num_str} (found at step {step + 1})."
        
        num_str = next_num_str
        step += 1
        
    if num_str in seen:
        cycle_start_step = seen[num_str]
        
        # If the number is a cycle, display the cycle members
        cycle_members = [k for k, v in seen.items() if v >= cycle_start_step]
        
        if len(cycle_members) == 1:
            return f"Start: {initial_number}. Result: The constant is {num_str} (found at step {step})."
        else:
            return f"Start: {initial_number}. Result: Converged to a cycle of length {len(cycle_members)} (Found at step {step}). Cycle: { ' -> '.join(cycle_members) }"
    
    return f"Start: {initial_number}. Result: Did not converge within {MAX_STEPS} steps."

def main():
    print("Welcome to the Kaprekar Constant/Cycle Finder!")
    print("This finds the result of the Kaprekar routine for a given number of digits (N).")
    
    while True:
        try:
            # 1. Ask for the number of digits
            digit_input = input("\nEnter the number of digits (e.g., 4 for 6174, or 5 for cycles): ")
            if digit_input.lower() in ['exit', 'quit']:
                print("Exiting application. Goodbye!")
                sys.exit()

            digit_count = int(digit_input)
            
            if digit_count < 3 or digit_count > 9:
                print("The Kaprekar routine is typically tested for 3 to 9 digits. Please try again.")
                continue

            # 2. Get the default starting number (e.g., 4321 for 4-digits)
            initial_number = get_starting_number(digit_count)
            print(f"Using the starting number: {initial_number}")

            # 3. Run the calculation and show the answer
            result = find_kaprekar_result(digit_count, initial_number)
            
            print("\n==============================================")
            print(result)
            print("==============================================\n")
            
        except ValueError:
            print("Invalid input. Please enter a whole number for the digit count.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
