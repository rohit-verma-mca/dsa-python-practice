"""
Question:
Implement merge sort - recursively split the list in half until each
piece has 1 element, then merge the pieces back together in sorted
order.

Topic     : Sorting, Merge Sort, Recursion
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    print(merge_sort([5, 2, 9, 1, 5, 6]))  # [1, 2, 5, 5, 6, 9]