# Program to Find the Greatest of Three Numbers

# Input three numbers from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Check which number is the greatest
if a >= b and a >= c:
    # If 'a' is greater than or equal to both 'b' and 'c'
    print(a, "is greatest")
elif b >= a and b >= c:
    # If above condition fails, check if 'b' is greater than or equal to both 'a' and 'c'
    print(b, "is greatest")
else:
    # If both conditions fail, 'c' is the greatest
    print(c, "is greatest")

# Time Complexity: O(1)
# Only a constant number of comparisons and operations are performed.

# Space Complexity: O(1)
# Only a fixed amount of space is used for three integer variables.
