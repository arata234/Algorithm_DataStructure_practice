def pascal(n: int):
    result = [[] for _ in range(n)]
    result[0].append(1)
    if n <= 1:
        return result
    
    result[1] = [1, 1]
    for i in range(2, n):
        result[i] = [result[i-1][j]+result[i-1][j+1] for j in range(len(result[i-1])-1)]
        result[i].append(1)
        result[i].insert(0,1)
    return result

from typing import List
def print_pascal(data: List[int]) -> None:
    len_list = len(data)
    for index, line in enumerate(data):
        line = [str(i) for i in line]
        if index > 0:
            for i in range(index):
                line.insert(2*i+1, " ")
        empty_num = len_list - index - 1
        empty_list = [" "]*empty_num
        line = empty_list + list(line) + empty_list
        print("".join(line))



if __name__ == "__main__":
    print_pascal(pascal(5))