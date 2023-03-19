import numpy as np
import time


def merge(data, start, mid, end):
    data_temp = []
    i = start
    j = mid + 1
    while i <= mid and j <= end:
        if data[i] < data[j]:
            data_temp.append(data[i])
            i = i + 1
        else:
            data_temp.append(data[j])
            j = j + 1

    while i <= mid:
        data_temp.append(data[i])
        i = i + 1

    while j <= end:
        data_temp.append(data[j])
        j = j + 1

    k = start
    for val in data_temp:
        data[k] = val
        k = k + 1  

def merge_sort(data, start, end):
    if start >= end:
        return
    
    mid = (start + end) // 2
    merge_sort(data, start, mid)
    merge_sort(data, mid + 1, end)
    merge(data, start, mid, end)


def is_sorted(sorted_array):
    for i in range(len(sorted_array)-1):
        if sorted_array[i] > sorted_array[i+1]:
            return False
    return True


if __name__ == "__main__":
    length = 10
    array = np.random.randint(0, 100, length)
    print(array)
    start = time.time()
    merge_sort(array, 0, length-1)
    print("time: ", time.time() - start)
    print(array)
    print(is_sorted)