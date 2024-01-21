# Input two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Print the original numbers
print(f"Original numbers: num1 = {num1}, num2 = {num2}")

# Swap using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Print the swapped numbers
print(f"After swapping: num1 = {num1}, num2 = {num2}")
