import numpy as np
import time


def selection_sort(unsorted_array):
    len_array = len(unsorted_array)
    start = 0
    end = len_array
    for i in range(start, end - 1):
        index = i
        for j in range(i+1, end):
            if unsorted_array[index] > unsorted_array[j]:
                index = j
        unsorted_array[i], unsorted_array[index] = unsorted_array[index], unsorted_array[i]
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
    array= selection_sort(unsorted_array)
    print("time: ", time.time() - start)
    print(array)
    print(is_sorted(array))