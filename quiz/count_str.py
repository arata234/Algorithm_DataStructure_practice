from typing import Tuple

def count_chars_v1(strings: str):
    strings = strings.lower()
    str_cnt = {}
    for char in strings:
        if not char.isspace():
            str_cnt[char] = str_cnt.get(char, 0) + 1
    
    return max(str_cnt, key=str_cnt.get)
    
    
    
if __name__ == "__main__":
    strings = "This is a pen. This is an apple. Applepen."
    print(count_chars_v1(strings))