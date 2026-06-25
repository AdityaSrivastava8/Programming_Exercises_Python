```python
import math  # For sqrt() function

n = int(input("Enter a number: "))

isPrime = True  # Assume the number is prime initially

if n <= 1:
    isPrime = False  # Numbers <= 1 are not prime
else:
    # Check divisors only up to sqrt(n) for efficiency
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            isPrime = False  # Found a divisor → not prime
            break            # Exit loop early

# Print result based on flag
if isPrime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a Prime Number.")

# Time Complexity: O(√n)
# We only check divisors up to sqrt(n), instead of all numbers up to n.

# Space Complexity: O(1)
# Only a constant amount of space is used (variables n, i, and isPrime).
```
