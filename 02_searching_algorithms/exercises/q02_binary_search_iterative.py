"""
Question:
Write a function that searches for a target value in a SORTED list
using binary search, implemented with a while loop (not recursion),
returning the index if found, or -1 if not found.

Topic     : Searching, Binary Search
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


def binary_search_iterative(sorted_lst, target):
    low = 0
    high = len(sorted_lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_lst[mid] == target:
            return mid
        elif sorted_lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search_iterative(numbers, 9))   # 4
    print(binary_search_iterative(numbers, 100)) # -1