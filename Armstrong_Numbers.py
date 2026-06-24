## Print Armstrong Numbers from 1 to 1000

print("Armstrong numbers from 1 to 1000:")

# Loop through numbers 1 to 1000
for n in range(1, 1001):
    temp = n          # Store current number
    sum = 0           # Initialize sum

    # Extract each digit
    while temp != 0:
        digit = temp % 10          # Get last digit
        sum += digit ** 3          # Add cube of digit
        temp //= 10                # Remove last digit

    # Check Armstrong condition
    if sum == n:
        print(n)

# Time Complexity: O(N × d)
# N = 1000 (numbers checked)
# d = number of digits in each number (max 4 for 1000)
# Effectively O(N)

# Space Complexity: O(1)
# Only a few variables (n, temp, sum, digit) are used


