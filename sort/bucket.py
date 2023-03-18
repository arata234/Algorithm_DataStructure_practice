import numpy as np
import time

import insertion

def bucket_sort(unsorted_array):
    len_array = len(unsorted_array)
    if len_array <= 1:
        return unsorted_array
    max_val = max(unsorted_array)
    bucket = [[] for _ in range(max_val+1)]
    #bucketごとに分ける
    for i in range(len_array):
        bucket_index = int(unsorted_array[i]*len_array / (max_val+1))
        bucket[bucket_index].append(unsorted_array[i])
    for i in range(max_val+1):
        bucket[i] = insertion.insertion_sort(bucket[i])
    result = []
    for i in range(max_val+1):
        result += bucket[i]
    return result
    

def is_sorted(sorted_array):
    for i in range(len(sorted_array)-1):
        if sorted_array[i] > sorted_array[i+1]:
            return False
    return True


if __name__ == "__main__":
    unsorted_array = np.random.randint(0, 10000, 100)
    start = time.time()
    array= bucket_sort(unsorted_array)
    print("time: ", time.time() - start)
    print(array)
    print(is_sorted(array))