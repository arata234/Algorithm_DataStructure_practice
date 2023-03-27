'''
from itertools import permutations
for r in permutations([1, 2, 3]):
    print(r)
'''

def permutation(my_list):
    if len(my_list) == 1:
        return [my_list]
    else:
        result = []                               
        for i, val in enumerate(my_list):
            rest = permutation(my_list[:i] + my_list[i+1:])
            for rest_perm in rest:
                perm = [val] + rest_perm   
                result.append(perm)
        return result
            
            
    
    
if __name__ == "__main__":
    l = [1, 2, 3]
    print(permutation(l))