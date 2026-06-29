import math

# Time Complexity: O(1)
# Space Complexity: O(1)

# Input principal amount
P = float(input("Enter Principal Amount: "))

# Input rate of interest
R = float(input("Enter Rate of Interest: "))

# Input time in years
T = float(input("Enter Time (in years): "))

# Calculate Simple Interest
# Formula: (P × R × T) / 100
SI = (P * R * T) / 100

# Calculate Compound Interest
# Formula: P × (1 + R/100)^T - P
CI = P * math.pow((1 + R / 100), T) - P

# Display Simple Interest (rounded to 2 decimal places)
print(f"\nSimple Interest = {SI:.2f}")

# Display Compound Interest (rounded to 2 decimal places)
print(f"Compound Interest = {CI:.2f}")
