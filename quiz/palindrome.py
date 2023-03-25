
def check_palindrome(strings: str) -> bool:
    if strings == strings[::-1]:
        return True
    return False


from typing import List
def find_palindrome(strings: str) -> List[str]:
    result = []
    
    for i in range(1, len(s)-1):
        x = 1
        while i-x >= 0 and i+x < len(s):
            if strings[i-x] == strings[i+x]:
                if i+x+1 == len(s):
                    result.append(strings[i-x:])
                else:
                    result.append(strings[i-x:i+x+1])
                x += 1
            else:
                break
    return result
    


if __name__ == "__main__":
    s = "abcdcba"
    # print(check_palindrome(s))
    print(find_palindrome(s))
    