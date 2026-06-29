# Hollow Rectangle Pattern in Python

rows = 5
cols = 7

# Time Complexity: O(rows × cols)
# Space Complexity: O(1)

# Outer loop controls rows
for i in range(1, rows + 1):

    # Inner loop controls columns
    for j in range(1, cols + 1):

        # Print '*' on the boundary cells
        if i == 1 or i == rows or j == 1 or j == cols:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    # Move to the next row
    print()
