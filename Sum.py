# Program to Find the Sum of Digits of a Number

# Input a number from the user
n = int(input("Enter a Number: "))

# Variable to store the sum of digits
sum = 0

# Loop until the number becomes 0
while n != 0:
    sum += n % 10   # Add the last digit of n to sum
    n //= 10        # Remove the last digit from n using integer division

# Print the result
print("Sum of Digits =", sum)

# Time Complexity: O(d)
# where d is the number of digits in n. Each iteration processes one digit.

# Space Complexity: O(1)
# Only a constant amount of extra space is used (sum and n).
