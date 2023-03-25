from typing import List, Tuple
def taci_cab_number(max_answer_num: int, match_answer_num: int) -> List[Tuple[int, List[Tuple[int, int]]]]:
    result = []
    answer = 1
    got_answer_num = 0
    while got_answer_num < max_answer_num:
        match_answer_count = 0
        ans_list = []
        max_param = int(pow(answer, 1.0/3)) + 1
        for x in range(1, max_param):
            for y in range(x, max_param):
                if x ** 3 + y ** 3 == answer:
                    match_answer_count += 1
                    ans_list.append((x, y))
        
        if match_answer_num == match_answer_count:
            result.append((answer, ans_list))
            got_answer_num += 1
        
        answer += 1
        print(answer)
    return result



if __name__ == "__main__":
    print(taci_cab_number(1, 2))