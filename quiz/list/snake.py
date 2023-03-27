from typing import List
import operator


def snake_str(chars: str, x: int) -> List[List[str]]:
    result = [[] for _ in range(x)]
    result_index = {i for i in range(x)}
    insert_index = int(x / 2)
    
    def pos(i):
        return i+1
    
    def neg(i):
        return i-1

    op = neg
    
    for s in chars:
        # insert_indexの位置, resultに格納
        result[insert_index].append(s)
        # それ以外のresultに" "を格納
        for rest_index in result_index - {insert_index}:
            result[rest_index].append(" ")
        if insert_index <= 0:
            op = pos
        if insert_index >= x-1:
            op = neg
        insert_index = op(insert_index)
    return result


if __name__ == "__main__":
    string = "0123456789" * 10
    strings = "".join(string)
    for line in snake_str(strings, 9):
        print("".join(line))