from typing import List
def order_even_odd_v1(numbers: List[int]) -> None:
    even_list, odd_list = [], []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    
    numbers[:] = even_list + odd_list
    
def order_even_odd_v2(numbers: List[int]) -> None:
    even_end_index = 0
    current_index = 0
    while current_index < len(numbers):
        print(current_index, even_end_index, numbers)
        if numbers[current_index] % 2 == 0:
            num = numbers.pop(current_index)
            numbers.insert(even_end_index, num)
            even_end_index += 1
            current_index += 1
        else:
            current_index += 1

def order_even_odd_v3(numbers: List[int]) -> None:
    i, j = 0, len(numbers) - 1
    while i < j:
        if numbers[i] % 2 == 0:
            i += 1
        else:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j -= 1


if __name__ == "__main__":
    numbers = [0, 1, 1, 1, 2, 2, 2, 3, 4, 4, 5, 6, 7]
    order_even_odd_v2(numbers)
    print(numbers)