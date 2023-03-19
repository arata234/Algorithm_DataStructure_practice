import numpy as np
import time 


def linear_search(numbers, value):
    for i in range(len(numbers)):
        if numbers[i] == value:
            return i
    return -1

def binary_search(numbers, value):
    left, right = 0, len(numbers)-1
    while left <= right:
        mid = (left+right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            left = mid + 1
        elif numbers[mid] > value:
            right = mid - 1
    return -1

def binary_search_rec(numbers, value):
    def _binary_search_rec(numbers, value, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search_rec(numbers, value, mid+1, right)
        else:
            return _binary_search_rec(numbers, value, left, mid-1)
    
    return _binary_search_rec(numbers, value, 0, len(numbers)-1)


if __name__ =="__main__":
    nums = np.random.randint(0, 1000000, 1000000)
    nums = sorted(nums)
    start = time.time()
    print(linear_search(nums, 999999))
    print(time.time()-start)
    start = time.time()
    print(binary_search(nums, 999999))
    print(time.time()-start)
    start = time.time()
    print(binary_search_rec(nums, 999999))
    print(time.time()-start)