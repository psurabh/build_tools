def sliding_window(array, window_size):
    subarrays = []
    for i in range(len(array) - window_size + 1):
        subarray = array[i:i + window_size]
        subarrays.append(subarray)
    return subarrays

if __name__ == "__main__":
    array1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    window_size1 = 3
    print(sliding_window(array1, window_size1))

    array2 = [10, 20, 30, 40, 50]
    window_size2 = 2
    print(sliding_window(array2, window_size2))

    array3 = [1, 2, 3]
    window_size3 = 1
    print(sliding_window(array3, window_size3))
