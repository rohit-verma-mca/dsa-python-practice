"""
Question:
Write a function that reverses a string using a stack (push every
character, then pop them all off).

Topic     : Stacks, Strings
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


def reverse_string_with_stack(s):
    stack = list(s)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str


if __name__ == "__main__":
    print(reverse_string_with_stack("hello"))   # olleh
    print(reverse_string_with_stack("Python"))  # nohtyP