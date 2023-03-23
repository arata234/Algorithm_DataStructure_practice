from typing import List
from collections import Counter

def min_count_remove(x: List, y: List):
    # x_d = {}
    # y_d = {}
    # for i in x:
    #     x_d[i] = x_d.get(i, 0) + 1
    # for i in y:
    #     y_d[i] = y_d.get(i, 0) + 1
    
    x_d = Counter(x)
    y_d = Counter(y)
    
    for key_x, value_x in x_d.items():
        value_y = y_d.get(key_x)
        if value_y:
            if value_x < value_y:
                x[:] = [i for i in x if i != key_x]
            elif value_x > value_y:
                y[:] = [i for i in y if i != key_x]
    return x, y
    
    print(x_d)
    print(y_d)



if __name__ == "__main__":
    x = [1, 2, 3, 4, 4, 5, 5, 8, 10]
    y = [4, 5, 5, 5, 6, 7, 8, 8, 10]
    print(x)
    print(y)
    x, y = min_count_remove(x, y)
    print(x)
    print(y)