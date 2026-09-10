"""
Question:
Implement bubble sort - repeatedly compare adjacent elements and swap
them if they're in the wrong order, until the list is sorted.

Topic     : Sorting, Bubble Sort
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


def bubble_sort(lst):
    arr = lst[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    print(bubble_sort([5, 2, 9, 1, 5, 6]))  # [1, 2, 5, 5, 6, 9]