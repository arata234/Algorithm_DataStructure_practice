import numpy as np
import time


def insertion_sort(unsorted_array):
    len_array = len(unsorted_array)
    for i in range(1, len_array):
        key = unsorted_array[i]
        j = i - 1
        while j >= 0 and key < unsorted_array[j]:
            unsorted_array[j+1] = unsorted_array[j]
            j -= 1
            unsorted_array[j+1] = key
    sorted_array = unsorted_array.copy()
    return sorted_array

def is_sorted(sorted_array):
    for i in range(len(sorted_array)-1):
        if sorted_array[i] > sorted_array[i+1]:
            return False
    return True


if __name__ == "__main__":
    unsorted_array = np.random.randint(0, 10000, 100)
    start = time.time()
    array= insertion_sort(unsorted_array)
    print("time: ", time.time() - start)
    print(array)
    print(is_sorted(array))