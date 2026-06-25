year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")

# Time Complexity: O(1)
# Only a fixed number of arithmetic and comparison operations are performed.

# Space Complexity: O(1)
# Uses only one integer variable regardless of input size.
