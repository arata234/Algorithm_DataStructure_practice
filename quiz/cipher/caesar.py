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
        index = (alphabet.index(char) + shift) % len(alphabet)
        result += alphabet[index]
    return result

def caesar_cipher_hack(text: str):
    for i in range(25):
        print(i, caesar_cipher(text, int(i)))



if __name__ == "__main__":
    print(caesar_cipher("BABA IS YOU is game", 3))
    caesar_cipher_hack("EDED LV BRX lv jdph")