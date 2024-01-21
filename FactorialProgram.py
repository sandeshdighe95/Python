# Accept an integer from the user
user_input = input("Enter a non-negative integer: ")

# Convert the user input to an integer
number = int(user_input)

# Check if the input is non-negative
if number < 0:
    print("Please enter a non-negative integer.")
else:
    # Initialize a variable 'factorial' to 1.
    factorial = 1

    # Calculate the factorial using a loop.
    for i in range(1, number + 1):
        factorial *= i

    # Print the result.
    print(f"The factorial of {number} is: {factorial}")
