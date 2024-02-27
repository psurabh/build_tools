"""
This file implements a binary search algorithm.
"""

def binary_search(lst, key):
    """
    Perform a binary search on a sorted list.

    Parameters:
    lst (list): The list to search.
    key (int): The value to search for.

    Returns:
    int: The index of the key in the list if found, otherwise -1.
    """
    if not lst:
        return -1
    if lst != sorted(lst):
        return -1

    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == key:
            return mid
        elif lst[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4, 5], 3))  # Expected output: 2
    print(binary_search([1, 2, 3, 4, 5], 6))  # Expected output: -1
    print(binary_search([], 1))  # Expected output: -1
    print(binary_search([2, 1], 1))  # Expected output: -1
