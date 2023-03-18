import numpy as np
import time


def in_order(numbers):
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
    # for i in range (len(numbers)-1):
    #     if numbers[i] > numbers[i+1]:
    #         return False
    # return True

def bogo_sort(unsorted_array):
    count = 0
    while not in_order(unsorted_array):
        np.random.shuffle(unsorted_array)
        count += 1
    sorted_array = unsorted_array.copy()
    return sorted_array, count
    
    
if __name__ == "__main__":
    unsorted_array = np.random.randint(0, 100, 10)
    start = time.time()
    array, count = bogo_sort(unsorted_array)
    print("time: ", time.time() - start)
    print(array, count)