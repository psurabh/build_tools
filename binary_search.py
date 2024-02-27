def binary_search(lst, target):
    """
    Perform a binary search on a sorted list.

    Parameters:
    lst (list): The list to search.
    target (int): The value to search for.

    Returns:
    int: The index of the target if found, None otherwise.
    """
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4, 5], 3))  # Expected output: 2
    print(binary_search([1, 2, 3, 4, 5], 6))  # Expected output: None
    print(binary_search([1, 2, 3, 4, 5, 6], 4))  # Expected output: 3
    print(binary_search([], 1))  # Expected output: None
