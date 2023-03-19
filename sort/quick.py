import numpy as np
import time


def partition(unsorted_array, low, high):
    i = low - 1
    pivot = unsorted_array[high]
    for j in range(low, high):
        if unsorted_array[j] <= pivot:
            i += 1
            unsorted_array[i], unsorted_array[j] = unsorted_array[j], unsorted_array[i]
    unsorted_array[i+1], unsorted_array[high] = unsorted_array[high], unsorted_array[i+1]
    return i+1

def quick_sort(unsorted_array):
    def _quick_sort(unsorted_array, low, high):
        if low < high:
            partition_index = partition(unsorted_array, low, high)
            _quick_sort(unsorted_array, low, partition_index-1)
            _quick_sort(unsorted_array, partition_index+1, high)
    _quick_sort(unsorted_array, 0, len(unsorted_array)-1)
    sorted_array = unsorted_array.copy()
    return sorted_array
    
def is_sorted(sorted_array):
    for i in range(len(sorted_array)-1):
        if sorted_array[i] > sorted_array[i+1]:
            return False
    return True


if __name__ == "__main__":
    unsorted_array = np.random.randint(0, 1000, 100)
    print(unsorted_array)
    start = time.time()
    array= quick_sort(unsorted_array)
    print("time: ", time.time() - start)
    print(array)
    print(is_sorted(array))