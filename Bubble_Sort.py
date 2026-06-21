# Bubble Sort in Python

# Time Complexity:
# Best Case   : O(n²)
# Average Case: O(n²)
# Worst Case  : O(n²)
#
# Space Complexity:
# O(1) -> Uses only a constant amount of extra space

# Input the number of elements
n = int(input("Enter the number of elements: "))

# Input array elements and store them in a list
arr = list(map(int, input(f"Enter {n} elements: ").split()))

# Bubble Sort starts
for i in range(n - 1):                 # Outer loop -> Runs (n-1) passes

    for j in range(n - i - 1):         # Inner loop -> Compares adjacent elements
                                       # Last i elements are already sorted

        if arr[j] > arr[j + 1]:        # If elements are in wrong order

            # Swap the elements
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Bubble Sort ends

# Display sorted array
print("Sorted array:")
for num in arr:
    print(num, end=" ")

"""
Complexity Analysis:

Time Complexity:
- Best Case   : O(n²)
  (This version still performs all passes even if array is sorted.)

- Average Case: O(n²)

- Worst Case  : O(n²)
  (Example: [5, 4, 3, 2, 1])

Space Complexity:
- O(1)
  Only loop variables are used; no extra list is created.

Number of Comparisons:
(n-1) + (n-2) + ... + 2 + 1
= n(n-1)/2

Hence Bubble Sort has O(n²) time complexity.
"""
