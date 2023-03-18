import numpy as np
import time


def gnome_sort(unsorted_array):
    len_array = len(unsorted_array)
    index = 0
    while index < len_array:
        if index == 0 or unsorted_array[index] >= unsorted_array[index-1]:
            index += 1
        else:
            unsorted_array[index], unsorted_array[index-1] = unsorted_array[index-1], unsorted_array[index]
            index -= 1
    
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
    array= gnome_sort(unsorted_array)
    print("time: ", time.time() - start)
    print(array)
    print(is_sorted(array))