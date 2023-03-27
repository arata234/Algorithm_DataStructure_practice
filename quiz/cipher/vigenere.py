import string

ALPHABET = string.ascii_uppercase

def generate_key(message: str, keyword: str) -> str:
    key = ""
    i = 0
    while len(key) != len(message):
        i = i % len(keyword)
        key += keyword[i]
        i += 1
    return key

def encrypt_v1(message: str, key: str) -> str:
    result = ""
    for i, char in enumerate(message):
        if char not in ALPHABET:
            result += char
            continue
        
        index = (ALPHABET.index(char) + ALPHABET.index(key[i])) % len(ALPHABET)
        result += ALPHABET[index]
    return result

def encrypt_v2(message: str, keyword: str):
    result = ""
    message = message.upper()
    keyword = keyword.upper()
    for i, char in enumerate(message):
        if char not in ALPHABET:
            result += char
            continue
        
        index = (ALPHABET.index(char) + ALPHABET.index(keyword[i % len(keyword)])) % len(ALPHABET)
        result += ALPHABET[index]
    return result

def decrypt_(ciphertext: str, key: str):
    result = ""
    ciphertext = ciphertext.upper()
    key = key.upper()
    for i, char in enumerate(ciphertext):
        if char not in ALPHABET:
            result += char
            continue

        index = (ALPHABET.index(char) - ALPHABET.index(key[i % len(key)]) + len(ALPHABET)) % len(ALPHABET)
        result += ALPHABET[index]
    return result


if __name__ =="__main__":
    # print(encrypt_v1("I AM MASTER", generate_key("I AM MASTER", "CAT")))
    print(encrypt_v2("I am master", "CAT"))
    print(decrypt_("K TO FCSMGR", "cat"))