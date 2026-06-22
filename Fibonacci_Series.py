# Fibonacci Series in Python

# Time Complexity:
# O(n) -> Loop runs n times
#
# Space Complexity:
# O(1) -> Only a few variables are used

# Ask user for number of terms
n = int(input("Enter number of terms: "))

# First two Fibonacci numbers
a = 0
b = 1

print("Fibonacci Series: ", end="")

# Print Fibonacci series up to n terms
for i in range(n):

    print(a, end=" ")      # Print current Fibonacci number

    next = a + b           # Compute next term
    a = b                  # Shift a to b
    b = next               # Shift b to next

print()

"""
Complexity Analysis:

Time Complexity:
- Best Case   : O(n)
- Average Case: O(n)
- Worst Case  : O(n)

Reason:
The loop executes exactly n times.

Space Complexity:
- O(1)

Reason:
Only three extra variables are used:
a, b, next

No additional list or array is created.
"""
