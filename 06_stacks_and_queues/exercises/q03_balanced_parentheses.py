"""
Question:
Write a function that checks whether a string of brackets
( ) [ ] { } is balanced - every opening bracket has a matching
closing bracket in the correct order.

Topic     : Stacks
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


def is_balanced(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    print(is_balanced("({[]})"))   # True
    print(is_balanced("([)]"))     # False
    print(is_balanced("((("))      # False