# Input a string from the user
user_input = input("Enter a string: ")

# Input the number of positions to rotate
rotation_count = int(input("Enter the number of positions to rotate: "))

# Calculate the rotated string
rotated_string = user_input[rotation_count % len(user_input):] + user_input[:rotation_count % len(user_input)]

# Print the rotated string
print(f"The rotated string is: {rotated_string}")
