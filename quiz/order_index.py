


from typing import List
def order_index_v1(chars: List[str], indexes:List[int]) -> str:
    temp = [None] * len(chars)
    for i, index in enumerate(indexes):
        temp[index] = chars[i]
    return "".join(temp)
    
def order_index_v2(chars: List[str], indexes:List[int]) -> str:
    i, len_indexes = 0, len(indexes) - 1
    while i < len_indexes:
        while i != indexes[i]:
            index = indexes[i]
            chars[index], chars[i] = chars[i], chars[index]
            indexes[index], indexes[i] = indexes[i], indexes[index]
        i += 1
    return "".join(chars)


if __name__ == "__main__":
    inp = ["h", "y", "n", "p", "t", "o"]
    ind = [3, 1, 5, 0, 2, 4]
    print(order_index_v2(inp, ind))