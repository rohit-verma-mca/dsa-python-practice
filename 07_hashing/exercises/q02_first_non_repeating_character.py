"""
Question:
Given a string, find the first character that doesn't repeat, using
a hash map to count character frequencies.

Topic     : Hashing, Strings
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


def first_non_repeating(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    for char in s:
        if char_counts[char] == 1:
            return char

    return None


if __name__ == "__main__":
    print(first_non_repeating("swiss"))     # w
    print(first_non_repeating("aabbcc"))    # None