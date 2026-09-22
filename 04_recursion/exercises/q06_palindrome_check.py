"""
Question:
Write a recursive function that checks whether a given string is a
palindrome (reads the same forwards and backwards).

Topic     : Recursion, Strings
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


if __name__ == "__main__":
    print(is_palindrome("madam"))   # True
    print(is_palindrome("python"))  # False
    print(is_palindrome("racecar")) # True