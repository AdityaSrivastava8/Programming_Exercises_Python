# Function to convert decimal to binary
def decimal_to_binary(num):
    # Handle the special case when the number is 0
    if num == 0:
        return "0"

    binary = ""  # Store the binary representation

    # Convert decimal to binary
    while num > 0:
        remainder = num % 2              # Get the remainder (0 or 1)
        binary = str(remainder) + binary # Add remainder to the beginning
        num //= 2                        # Divide the number by 2

    return binary


# Function to convert binary to decimal
def binary_to_decimal(binary):
    decimal = 0  # Store the decimal equivalent
    power = 0    # Represents the power of 2

    # Process digits from right to left
    for digit in reversed(binary):
        decimal += int(digit) * (2 ** power)
        power += 1

    return decimal


# Display menu
print("===== Number System Converter =====")
print("1. Decimal to Binary")
print("2. Binary to Decimal")

# Take user's choice
choice = int(input("Enter your choice (1 or 2): "))

# Perform the selected conversion
if choice == 1:
    decimal = int(input("Enter a decimal number: "))

    if decimal < 0:
        print("Please enter a non-negative integer.")
    else:
        print(f"Binary equivalent = {decimal_to_binary(decimal)}")

elif choice == 2:
    binary = input("Enter a binary number: ")

    # Validate the binary input
    if all(bit in "01" for bit in binary):
        print(f"Decimal equivalent = {binary_to_decimal(binary)}")
    else:
        print("Invalid binary number. Please enter only 0s and 1s.")

else:
    print("Invalid choice. Please select either 1 or 2.")

# Time Complexity:
# Decimal to Binary: O(log n)
# Binary to Decimal: O(n)

# Space Complexity:
# Decimal to Binary: O(log n)
# Binary to Decimal: O(1)
