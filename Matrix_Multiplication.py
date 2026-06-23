# Element-wise Multiplication of Two Arrays

# Time Complexity: O(n)
# Space Complexity: O(n)

# First array
a = [1, 2, 3, 4, 5]

# Second array
b = [6, 7, 8, 9, 10]

# Array to store multiplication results
result = []

# Multiply corresponding elements
for i in range(len(a)):      # Runs n times
    result.append(a[i] * b[i])

# Display result array
print("Result array:", end=" ")

for num in result:           # Runs n times
    print(num, end=" ")

print() 
