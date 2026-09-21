"""
Question:
Write a recursive function that returns a string reversed, without
using slicing shortcuts like s[::-1].

Topic     : Recursion, Strings
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


if __name__ == "__main__":
    print(reverse_string("hello"))   # olleh
    print(reverse_string("Python"))  # nohtyP