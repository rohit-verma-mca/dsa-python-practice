"""
Question:
Run all 5 sorting algorithms on lists of increasing size and time
each one, printing a comparison table to see which algorithms scale
well and which don't.

Topic     : Sorting, Algorithm Comparison
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""

import time
import random

from q01_bubble_sort import bubble_sort
from q02_selection_sort import selection_sort
from q03_insertion_sort import insertion_sort
from q04_merge_sort import merge_sort
from q05_quick_sort import quick_sort


def time_sort(sort_func, data):
    start = time.time()
    sort_func(data)
    return time.time() - start


def solve():
    sizes = [100, 500, 1000]
    algorithms = {
        "Bubble": bubble_sort,
        "Selection": selection_sort,
        "Insertion": insertion_sort,
        "Merge": merge_sort,
        "Quick": quick_sort,
    }

    for size in sizes:
        data = [random.randint(1, 10000) for _ in range(size)]
        print(f"\nList size: {size}")
        for name, func in algorithms.items():
            elapsed = time_sort(func, data)
            print(f"  {name:<12}{elapsed:.6f} sec")


if __name__ == "__main__":
    solve()