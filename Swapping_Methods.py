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
# Method 12: Walrus Operator
# TC: O(1), SC: O(1)
# Uses assignment expression (:=) inside a tuple
# ---------------------------------------------------
print(f"Before Swap: a = {a}, b = {b}")
a, b = (temp := b), a
print(f"After Swap: a = {a}, b = {b}")

# ---------------------------------------------------
# Method 13: List Slicing
# TC: O(1), SC: O(1)
# Uses slicing to reverse the list
# ---------------------------------------------------
x, y = [a, b][::-1]
print(f"Method 13 (List Slicing): a = {x}, b = {y}")


# ---------------------------------------------------
# Method 14: Class-Based Swap
# TC: O(1), SC: O(1)
# Uses Object-Oriented Programming
# ---------------------------------------------------
class Swapper:
    def __init__(self, a, b):
        self.a = b
        self.b = a

obj = Swapper(a, b)
x, y = obj.a, obj.b
print(f"Method 14 (Class-Based): a = {x}, b = {y}")


# ---------------------------------------------------
# Method 15: Complex Number Trick
# TC: O(1), SC: O(1)
# Uses real and imaginary parts
# ---------------------------------------------------
z = complex(a, b)

x = int(z.imag)
y = int(z.real)

print(f"Method 15 (Complex Number): a = {x}, b = {y}")


# ---------------------------------------------------
# Method 16: operator.xor() Swap
# TC: O(1), SC: O(1)
# Functional Programming Style
# ---------------------------------------------------
from operator import xor

x, y = a, b

x = xor(x, y)
y = xor(x, y)
x = xor(x, y)

print(f"Method 16 (operator.xor): a = {x}, b = {y}")


# ---------------------------------------------------
# Method 17: NumPy Indexing Swap
# TC: O(1), SC: O(1)
# Uses NumPy Advanced Indexing
# ---------------------------------------------------
import numpy as np

arr = np.array([a, b])

arr[[0, 1]] = arr[[1, 0]]

x, y = arr

print(f"Method 17 (NumPy): a = {x}, b = {y}")


# ---------------------------------------------------
# Method 18: reversed() Function
# TC: O(1), SC: O(1)
# Uses Python Built-in Iterator
# ---------------------------------------------------
x, y = reversed((a, b))

print(f"Method 18 (reversed): a = {x}, b = {y}")


# ---------------------------------------------------
# Method 19: globals() Swap
# TC: O(1), SC: O(1)
# Uses Global Namespace Manipulation
# ---------------------------------------------------
g_a, g_b = a, b

globals()['g_a'], globals()['g_b'] = globals()['g_b'], globals()['g_a']

print(f"Method 19 (globals): a = {g_a}, b = {g_b}")


# ---------------------------------------------------
# Method 20: exec() Swap
# TC: O(1), SC: O(1)
# Executes Python Code Dynamically
# ---------------------------------------------------
e_a, e_b = a, b

exec("e_a, e_b = e_b, e_a")

print(f"Method 20 (exec): a = {e_a}, b = {e_b}")


# ---------------------------------------------------
# Method 21: Set-Based Swap
# TC: O(1), SC: O(1)
# Unreliable - Sets Are Unordered
# ---------------------------------------------------
try:
    x, y = {*{a, b}}
    print(f"Method 21 (Set-Based): a = {x}, b = {y}")
except ValueError:
    print("Method 21 (Set-Based): Failed because set order is not guaranteed")

