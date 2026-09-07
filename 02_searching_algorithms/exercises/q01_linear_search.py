"""
Question:
Write a function that searches for a target value in a list by
checking each element one at a time, returning the index if found,
or -1 if not found.

Topic     : Searching, Linear Search
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    numbers = [4, 2, 9, 7, 5, 1]
    print(linear_search(numbers, 7))    # 3
    print(linear_search(numbers, 100))  # -1