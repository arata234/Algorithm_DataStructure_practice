class Stack(object):
    def __init__(self):
        self.stack = []
    
    def push(self, data) -> None:
        self.stack.append(data)
    
    from typing import Any
    def pop(self) -> Any:
        return self.stack.pop()


def validate_format(chars: str) -> bool:
    lookup = {"[":"]", "(":")", "{":"}"}
    stack = []
    for char in chars:
        if char in lookup.keys():
            stack.append(lookup[char])
        if char in lookup.values():
            if stack == []:
                return False
            if char != stack.pop():
                return False
    
    if stack:
        return False
    
    return True

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.stack)
    print(stack.pop())