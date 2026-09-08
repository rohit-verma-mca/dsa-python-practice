"""
Question:
Write the same binary search logic as Q2, but implemented recursively
instead of with a loop.

Topic     : Searching, Binary Search, Recursion
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


def binary_search_recursive(sorted_lst, target, low=0, high=None):
    if high is None:
        high = len(sorted_lst) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if sorted_lst[mid] == target:
        return mid
    elif sorted_lst[mid] < target:
        return binary_search_recursive(sorted_lst, target, mid + 1, high)
    else:
        return binary_search_recursive(sorted_lst, target, low, mid - 1)


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search_recursive(numbers, 5))    # 2
    print(binary_search_recursive(numbers, 100))  # -1