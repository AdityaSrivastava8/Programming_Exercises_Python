# Swap Two Numbers Using Multiple Methods

a, b = map(int, input("Enter two numbers: ").split())

print(f"\nOriginal Values: a = {a}, b = {b}")

# ---------------------------------------------------
# Method 1: Temporary Variable
# TC: O(1), SC: O(1)
# ---------------------------------------------------
x, y = a, b
temp = x
x = y
y = temp
print(f"\nMethod 1 (Temp Variable): a = {x}, b = {y}")

# ---------------------------------------------------
# Method 2: Tuple Unpacking
# TC: O(1), SC: O(1)
# ---------------------------------------------------
x, y = a, b
x, y = y, x
print(f"Method 2 (Tuple Unpacking): a = {x}, b = {y}")

# ---------------------------------------------------
# Method 3: Addition/Subtraction
# TC: O(1), SC: O(1)
# ---------------------------------------------------
x, y = a, b
x = x + y
y = x - y
x = x - y
print(f"Method 3 (Arithmetic): a = {x}, b = {y}")

# ---------------------------------------------------
# Method 4: Multiplication/Division
# TC: O(1), SC: O(1)
# Limitation: Doesn't work when a or b is 0
# ---------------------------------------------------
if a != 0 and b != 0:
    x, y = a, b
    x = x * y
    y = x // y
    x = x // y
    print(f"Method 4 (Multiply/Divide): a = {x}, b = {y}")

# ---------------------------------------------------
# Method 5: XOR Swap
# TC: O(1), SC: O(1)
# Works only for integers
# ---------------------------------------------------
x, y = a, b
x ^= y
y ^= x
x ^= y
print(f"Method 5 (XOR): a = {x}, b = {y}")

# ---------------------------------------------------
# Method 6: Lambda Function
# TC: O(1), SC: O(1)
# ---------------------------------------------------
x, y = (lambda p, q: (q, p))(a, b)
print(f"Method 6 (Lambda): a = {x}, b = {y}")

# ---------------------------------------------------
# Method 7: List Swapping
# TC: O(1), SC: O(1)
# ---------------------------------------------------
lst = [a, b]
lst[0], lst[1] = lst[1], lst[0]
print(f"Method 7 (List): a = {lst[0]}, b = {lst[1]}")

# ---------------------------------------------------
# Method 8: Dictionary Swapping
# TC: O(1), SC: O(1)
# ---------------------------------------------------
d = {"a": a, "b": b}
d["a"], d["b"] = d["b"], d["a"]
print(f"Method 8 (Dictionary): a = {d['a']}, b = {d['b']}")

# ---------------------------------------------------
# Method 9: Function Return
# TC: O(1), SC: O(1)
# ---------------------------------------------------
def swap(x, y):
    return y, x

x, y = swap(a, b)
print(f"Method 9 (Function): a = {x}, b = {y}")

# ---------------------------------------------------
# Method 10: Dunder (__xor__) Method
# TC: O(1), SC: O(1)
# Advanced Python Internals
# ---------------------------------------------------
x, y = (
    a.__xor__(b).__xor__(a),
    a.__xor__(b).__xor__(b)
)
print(f"Method 10 (Dunder XOR): a = {x}, b = {y}")

# ---------------------------------------------------
# Method 11: Nested Lambda + Tuple
# TC: O(1), SC: O(1)
# ---------------------------------------------------
x, y = (lambda p: (p[1], p[0]))((a, b))
print(f"Method 11 (Nested Lambda): a = {x}, b = {y}")

# ---------------------------------------------------
# Method 12: Pythonic One-Liner
# TC: O(1), SC: O(1)
# ---------------------------------------------------
x, y = a, b
x, y = y, x
print(f"Method 12 (Pythonic One-Liner): a = {x}, b = {y}")
