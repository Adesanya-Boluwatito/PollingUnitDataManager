#                        Task 7
def recursive_binary_search(arr, target, low, high):
    """
    # Recursive Binary Search
    # :param arr: Sorted list of numbers
    # :param target: Number to search for
    # :param low: Lower bound of the current search interval
    # :param high: Upper bound of the current search interval
    # :return: Index of the target if found, otherwise -1
    # """
    if low <= high:
        mid = (low + high) // 2

        # Check if the middle element is the target
        if arr[mid] == target:
            return mid
        # If the target is smaller than the middle element, search in the left subarray
        elif arr[mid] > target:
            return recursive_binary_search(arr, target, low, mid - 1)
        # If the target is larger than the middle element, search in the right subarray
        else:
            return recursive_binary_search(arr, target, mid + 1, high)
    else:
        # Element is not present in the list
        return -1


# TEST ARRAY
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Input from the user
user_input = int(input("Enter a number to search for: "))

# Perform the search
result = recursive_binary_search(numbers, user_input, 0, len(numbers) - 1)

# Display the result
if result != -1:
    print(f"{user_input} found at index {result}.")
else:
    print(f"{user_input} not found in the list.")