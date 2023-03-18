import numpy as np
import time


def cocktail_sort(unsorted_array):
    len_array = len(unsorted_array)
    swapped = True
    start = 0
    end = len_array - 1
    c = 0
    while swapped:
        swapped = False
        for i in range(start, end):
            if unsorted_array[i] > unsorted_array[i+1]:
                swapped = True
                unsorted_array[i], unsorted_array[i+1] = unsorted_array[i+1], unsorted_array[i]
        c += 1
        if not swapped:
            break
        
        swapped = False
        end -=1
        for i in range(end-1, start-1, -1):
            if unsorted_array[i] > unsorted_array[i+1]:
                swapped = True
                unsorted_array[i], unsorted_array[i+1] = unsorted_array[i+1], unsorted_array[i]
        start += 1
        c += 1
        
    sorted_array = unsorted_array.copy()
    return sorted_array, c


if __name__ == "__main__":
    unsorted_array = np.random.randint(0, 100, 100)
    start = time.time()
    array, c = cocktail_sort(unsorted_array)
    print("time: ", time.time() - start)
    print(array, c)