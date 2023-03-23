from typing import List, Iterator, Tuple
def find_pair(pairs: List[Tuple[int, int]]) -> Iterator[tuple[int, int]]:
    cache = {}
    for pair in pairs:
        second = pair[1]
        cache[second] = []
    
    for pair in pairs:
        first, second = pair[0], pair[1]
        cache[second].append(first)

    for pair in pairs:
        first, second = pair[0], pair[1]
        if first in cache:
            for value in cache[first]:
                if value == second:
                    print(pair)
        


if __name__ == "__main__":
    input = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    find_pair(input)