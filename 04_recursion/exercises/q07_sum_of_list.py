"""
Question:
Write a recursive function that returns the sum of all elements in a
list of numbers, without using the built-in sum().

Topic     : Recursion, Lists
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


def sum_list(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + sum_list(lst[1:])


if __name__ == "__main__":
    print(sum_list([1, 2, 3, 4, 5]))  # 15
    print(sum_list([]))               # 0