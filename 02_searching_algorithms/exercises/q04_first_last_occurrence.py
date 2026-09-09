"""
Question:
Given a sorted list that may contain duplicate values, write a
function that finds the first and last index of a target value using
binary search (not a plain linear scan), returning a tuple
(first_index, last_index), or (-1, -1) if not found.

Topic     : Searching, Binary Search
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


def find_first(sorted_lst, target):
    low, high = 0, len(sorted_lst) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if sorted_lst[mid] == target:
            result = mid
            high = mid - 1  # keep searching left for an earlier occurrence
        elif sorted_lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result


def find_last(sorted_lst, target):
    low, high = 0, len(sorted_lst) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if sorted_lst[mid] == target:
            result = mid
            low = mid + 1  # keep searching right for a later occurrence
        elif sorted_lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result


def find_first_and_last(sorted_lst, target):
    return (find_first(sorted_lst, target), find_last(sorted_lst, target))


if __name__ == "__main__":
    numbers = [1, 2, 2, 2, 3, 4, 5]
    print(find_first_and_last(numbers, 2))    # (1, 3)
    print(find_first_and_last(numbers, 100))  # (-1, -1)