# Input a string from the user
user_input = input("Enter a string: ")

# Define the set of vowels
vowels = set("aeiouAEIOU")

# Replace vowels with underscores
modified_string = ''.join('_' if char in vowels else char for char in user_input)

# Print the modified string
print(f"The modified string is: {modified_string}")
