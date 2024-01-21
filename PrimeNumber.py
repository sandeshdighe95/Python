# take input from the user
number = int(input("Enter a positive number: "))
is_prime = True

# check if the number is equal to 1
if number == 1:
    print("1 is neither prime nor composite number.")

# check if the number is greater than 1
elif number > 1:

    # looping through 2 to number-1
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

# check if the number is less than 1
else:
    print("The number is not a prime number.")
