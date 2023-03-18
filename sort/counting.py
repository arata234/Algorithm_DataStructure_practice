import numpy as np
import time

def counting_sort(unsorted_array):
    max_val = max(unsorted_array)
    counts = [0 for i in range(max_val+1)]
    for val in unsorted_array:
        counts[val] += 1
    print(counts)
    
    sorted_array = []
    for i, v in enumerate(counts):
        sorted_array += [i]*v
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
    array= counting_sort(unsorted_array)
    print("time: ", time.time() - start)
    print(array)
    print(is_sorted(array))