from typing import List


def remove_duplication_v1(numbers: List[int]) -> List[int]:
    new_list = []
    for num in numbers:
        if num not in new_list:
            new_list.append(num)
    return new_list 

def remove_duplication_v2(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    i = 0
    while i != len_numbers-1:
        if numbers[i] == numbers[i+1]:
            numbers.pop(i+1)
            len_numbers = len(numbers)
        else:
            i += 1
    
    return numbers

def remove_duplication_v3(numbers: List[int]) -> List[int]:
    i = len(numbers) - 1
    while i > 0:
        if numbers[i] == numbers[i-1]:
            numbers.pop(i)
        i -= 1
    return numbers
    

if __name__ == "__main__":
    l = [1, 3, 3, 5, 5, 7, 7, 7, 10, 12, 12, 15]
    print(remove_duplication_v1(l))
    print(remove_duplication_v2(l))
    print(remove_duplication_v3(l))