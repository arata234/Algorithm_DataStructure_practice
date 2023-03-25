NUM_ALPHABET_MAPPING = {
    0: "+",
    1: "0",
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WXYZ"
}

from typing import List
def phone_memonic_v1(phone_number: str) -> List[str]:
    result = []
    phone_number_list = [int(s) for s in phone_number.replace("-", "")]
    temp = [""] * len(phone_number_list)
    def find_alphabet(digit: int=0) -> None:
        if digit == len(phone_number_list):
            result.append("".join(temp))
        else:
            for char in NUM_ALPHABET_MAPPING[phone_number_list[digit]]:
                temp[digit] = char
                find_alphabet(digit+1)
    find_alphabet()
    return result

def phone_memonic_v2(phone_number: str) -> List[str]:
    result = []
    phone_number_list = [int(s) for s in phone_number.replace("-", "")]
    
    # stackで全通りを見つける
    stack = [""]
    while len(stack) != 0:
        alphabets = stack.pop()
        if len(alphabets) == len(phone_number):
            result.append("".join(alphabets))
        else:
            for char in NUM_ALPHABET_MAPPING[phone_number_list[len(alphabets)]]:
                stack.append(alphabets+char)
            print(stack)
    return result


if __name__ == "__main__":
    phone_number = "568-379-8466"
    phone_number = "5683"
    print(phone_memonic_v2(phone_number))