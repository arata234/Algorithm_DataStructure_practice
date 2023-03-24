from typing import List

def list_to_int_plus_one(numbers: List[int]) -> int:
    i = 0
    while numbers[i] == 0:
        numbers.pop(0)
        
    for i in range(len(numbers)):
        if numbers[-1*(i+1)] != 9:
            numbers[-1*(i+1)] += 1
            break
        else:
            numbers[-1*(i+1)] = 0
        
    if numbers[0] == 0:
        numbers.insert(0,1)

    print(numbers)
    ans = [x*(10)**(i) for i, x in enumerate(reversed(numbers))]
    return sum(ans)







if __name__ == "__main__":
    input = [1]
    input = [2, 3]
    input = [9, 9]
    input = [7, 8, 9]
    input = [0, 0, 9, 9, 9, 9]
    input = [0, 0, 9, 0, 9]
    print(list_to_int_plus_one(input))