"""
Question:
Implement a Stack class with push, pop, peek, and is_empty methods,
using a Python list internally.

Topic     : Stacks
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())  # 3
    print(s.pop())   # 3
    print(s.pop())   # 2
    print(s.is_empty())  # False