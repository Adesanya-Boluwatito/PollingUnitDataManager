
                # ***** Task 8 ******
def fibonacci(n):
    """
    Generate the Fibonacci sequence up to the nth term
    """
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


def sum_fibonacci(n):
    """
    Calculate the sum of the first n Fibonacci numbers
    """
    fib_numbers = fibonacci(n)
    return sum(fib_numbers)

# Calculate and print the sum of the first 50 Fibonacci numbers
result = sum_fibonacci(50)
print(f"Sum of the first 50 Fibonacci numbers: {result}")