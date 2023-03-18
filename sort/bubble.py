import numpy as np
import time


def bubble_sort(unsorted_array):
    len_array = len(unsorted_array)
    for i in range(len_array):
        for j in range(len_array-i-1):
            if unsorted_array[j] > unsorted_array[j+1]:
                unsorted_array[j], unsorted_array[j+1] = unsorted_array[j+1], unsorted_array[j]
    sorted_array = unsorted_array.copy()
    return sorted_array

if __name__ == "__main__":
    unsorted_array = np.random.randint(0, 100, 100)
    start = time.time()
    array= bubble_sort(unsorted_array)
    print("time: ", time.time() - start)
    print(array)