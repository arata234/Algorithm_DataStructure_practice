from typing import List
import random

def generate_triangle_list(depth: int, max_num: int) -> List[List[int]]:
    return [[random.randint(0, max_num) for _ in range(i)] for i in range(1, depth+1)]
