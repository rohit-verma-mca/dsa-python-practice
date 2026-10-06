"""
Question:
Implement a stack that supports push, pop, and get_min, where
get_min returns the minimum element currently in the stack, all in
O(1) time.

Topic     : Stacks
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # tracks the minimum at each point

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if not self.stack:
            raise IndexError("pop from empty stack")
        self.min_stack.pop()
        return self.stack.pop()

    def get_min(self):
        if not self.min_stack:
            raise IndexError("get_min from empty stack")
        return self.min_stack[-1]


if __name__ == "__main__":
    ms = MinStack()
    ms.push(5)
    ms.push(2)
    ms.push(8)
    print(ms.get_min())  # 2
    ms.pop()
    print(ms.get_min())  # 2
    ms.pop()
    print(ms.get_min())  # 5