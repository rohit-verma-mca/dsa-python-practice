"""
Question:
Implement insertion sort - build the sorted list one element at a
time, inserting each new element into its correct position among the
already-sorted elements.

Topic     : Sorting, Insertion Sort
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


def insertion_sort(lst):
    arr = lst[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    print(insertion_sort([5, 2, 9, 1, 5, 6]))  # [1, 2, 5, 5, 6, 9]