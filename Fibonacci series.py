fibonacci_sequence = [0, 1]

for _ in range(8):
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)


print(f" first 10 fibonacci number are: {fibonacci_sequence}")