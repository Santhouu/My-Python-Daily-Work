# Swap two numbers using a temporary variable
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"Before Swap: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"After Swap: a = {a}, b = {b}")
