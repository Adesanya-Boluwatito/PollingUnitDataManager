import random
                               # ***** Task 8 *******


def generate_random_binary():
    """
    Generate a random 4-digit binary number
    """
    return ''.join(random.choice('01') for _ in range(4))


def binary_to_decimal(binary_str):
    """
    Convert a binary number to decimal
    """
    return int(binary_str, 2)


# Generate a random 4-digit binary number
random_binary = generate_random_binary()

# Convert the binary number to decimal
decimal_result = binary_to_decimal(random_binary)

# Print the results
print(f"Generated Binary: {random_binary}")
print(f"Converted to Decimal: {decimal_result}")
