# Function to calculate factorial
def factorial(n):
    fact = 1  # Initialize result variable

    # Loop from 1 to n
    for i in range(1, n + 1):
        fact *= i  # Multiply fact by current number

    return fact  # Return the final factorial value


# Take input from the user
num = int(input("Enter a number: "))

# Check if the number is negative
if num < 0:
    # Factorial is not defined for negative numbers
    print("Factorial is not defined for negative numbers.")
else:
    # Call the factorial function and display the result
    print(f"Factorial of {num} = {factorial(num)}")

# Time Complexity: O(n)
# Space Complexity: O(1)
