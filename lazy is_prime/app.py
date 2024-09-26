# if n > 3
def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    if ((n * n) - 1) % 24 == 0:
        return True
    return False

n = int(input("Enter a number (greater of 3): "))
if is_prime(n):
    print(n, "is probably prime.")
else:
    print(n, "is definitely not prime.")
