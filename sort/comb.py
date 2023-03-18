import numpy as np
import time


def comb_sort(unsorted_array):
    len_array = len(unsorted_array)
    gap = len_array
    swapped = True
    
    while gap != 1 or swapped:
        gap = int(gap/1.3)
        
        if gap < 1:
            gap = 1
        swapped = False
        for i in range(len_array - gap):
            if unsorted_array[i] > unsorted_array[i+gap]:
                unsorted_array[i], unsorted_array[i+gap] = unsorted_array[i+gap], unsorted_array[i]
                swapped = True
        
    sorted_array = unsorted_array.copy()
    return sorted_array


if __name__ == "__main__":
    unsorted_array = np.random.randint(0, 10000, 100)
    start = time.time()
    array= comb_sort(unsorted_array)
    print("time: ", time.time() - start)
    print(array)