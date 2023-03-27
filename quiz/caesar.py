import string


def caesar_cipher(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isupper():
            alphabet = string.ascii_uppercase
        elif char.islower():
            alphabet = string.ascii_lowercase
        else:
            result += char
            continue
    print(alphabet)

if __name__ == "__main__":
    