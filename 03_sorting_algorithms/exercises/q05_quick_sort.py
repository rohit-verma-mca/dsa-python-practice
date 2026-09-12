"""
Question:
Implement quick sort - pick a pivot element, partition the list so
smaller elements go left and larger go right, then recursively sort
each side.

Topic     : Sorting, Quick Sort, Recursion
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    print(quick_sort([5, 2, 9, 1, 5, 6]))  # [1, 2, 5, 5, 6, 9]