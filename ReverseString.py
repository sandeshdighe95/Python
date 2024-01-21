# Input a string from the user
user_input = input("Enter a string: ")

# Initialize an empty string to store the reversed string
reversed_string = ""

# Iterate through the characters of the input string in reverse order
for char in reversed(user_input):
    reversed_string += char

# Print the reversed string
print(f"The reversed string is: {reversed_string}")
