import numpy as np

a = np.arange(9, dtype=float).reshape(3,3)
print("First array")
print(a)
print("\n")

b = np.array([10,10,10])
print("Second array")
print(b)
print("\n")

print("Adding the two arrays")
print(np.add(a, b))
print("\n")

print("Subtracting the two arrays")
print(np.subtract(a, b))
print("\n")

print("Multiplying the two arrays")
print(np.multiply(a, b))
print("\n")

print("Dividing the two arrays")
print(np.divide(a, b))
print("\n") 