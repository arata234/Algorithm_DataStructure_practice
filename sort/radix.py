import numpy as np
import time


def counting_sort(unsorted_array, place):
    counts = [0 for i in range(10)]
    result = [0 for i in range(len(unsorted_array))]
    for val in unsorted_array:
        index = int(val / place) % 10
        counts[index] += 1
    print(counts)
    
    for i in range(1,10):
        counts[i] += counts[i-1]
        
    i = len(unsorted_array) - 1
    while i >= 0:
        index = int(unsorted_array[i] / place) % 10
        result[counts[index]-1] = unsorted_array[i]
        counts[index] -= 1
        i -= 1
    sorted_array = result.copy()
    return sorted_array
    
def radix_sort(unsorted_array):
    max_val = max(unsorted_array)
    place = 1
    while max_val > place:
        unsorted_array = counting_sort(unsorted_array, place)
        place *= 10
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
    array= radix_sort(unsorted_array)
    print("time: ", time.time() - start)
    print(array)
    print(is_sorted(array))