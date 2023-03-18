import numpy as np
import time


def shell_sort(unsorted_array):
    len_array = len(unsorted_array)
    gap = len_array // 2
    while gap > 0:
        for i in range(gap, len_array):
            temp = unsorted_array[i]
            j = i
            while j >= gap and unsorted_array[j-gap] > temp:
                unsorted_array[j] = unsorted_array[j-gap]
                j -= gap
            unsorted_array[j] = temp
        gap //= 2
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
    array= shell_sort(unsorted_array)
    print("time: ", time.time() - start)
    print(array)
    print(is_sorted(array))