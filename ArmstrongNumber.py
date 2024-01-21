# Input a number from the user
number = int(input("Enter a number: "))

# Convert the number to a string to find its length (number of digits)
num_str = str(number)
num_digits = len(num_str)

# Calculate the sum of each digit raised to the power of the number of digits
sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

# Check if the number is an Armstrong number
if number == sum_of_digits:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
