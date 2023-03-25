
def generate_prime_numbers(num: int) -> list:
    prime_list = []
    current_number = 2
    while current_number <= num:
        b = [True if current_number % i != 0 else False for i in prime_list]
        if all(b):
            prime_list.append(current_number)
            current_number += 1
        else:
            current_number += 1
            
    return prime_list
            
def is_prime(numbers: list) -> bool:
    prime_list = generate_prime_numbers(max(numbers))
    b = [True if i in prime_list else False  for i in numbers]
    
    return all(b)

if __name__ == "__main__":
    num = 100
    numbers = [2, 3, 999, 5]
    # print(generate_prime_numbers(num))
    print(is_prime(numbers))