"""
Question:
Implement selection sort - repeatedly find the minimum element from
the unsorted part of the list and move it to the front.

Topic     : Sorting, Selection Sort
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


def selection_sort(lst):
    arr = lst[:]
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == "__main__":
    print(selection_sort([5, 2, 9, 1, 5, 6]))  # [1, 2, 5, 5, 6, 9]