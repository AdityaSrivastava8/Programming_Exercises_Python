# Reverse a Number in Python

# Time Complexity:
# O(d) -> d = number of digits in the number
#
# Space Complexity:
# O(1) -> Uses only a few variables

# Input number
n = int(input("Enter a Number: "))

# Variable to store reversed number
rev = 0

# Loop runs until n becomes 0
while n != 0:

    rev = rev * 10 + (n % 10)   # Extract last digit and append to rev
    n //= 10                    # Remove last digit from n

# Display reversed number
print("Reverse =", rev)

"""
Complexity Analysis:

Time Complexity:
- Best Case   : O(d)
- Average Case: O(d)
- Worst Case  : O(d)

Reason:
Each digit of the number is processed exactly once.

Space Complexity:
- O(1)

Reason:
Only a few integer variables (n and rev) are used.
No extra list, array, or string is created.
"""
