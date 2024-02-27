"""
This file implements a binary search algorithm.
"""

def binary_search(sorted_list, search_key):
    """
    Perform a binary search on a sorted list.

    Parameters:
    sorted_list (list): The sorted list to search.
    search_key (int): The value to search for.

    Returns:
    int: The index of the key in the list if found, otherwise -1.
    """
    if not sorted_list:
        return -1
    if sorted_list != sorted(sorted_list):
        return -1

    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == search_key:
            return mid
        elif sorted_list[mid] < search_key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    print(binary_search([1, 2, 3, 4, 5], 3))  # Expected output: 2
    print(binary_search([1, 2, 3, 4, 5], 6))  # Expected output: -1
    print(binary_search([], 1))  # Expected output: -1
    print(binary_search([2, 1], 1))  # Expected output: -1
