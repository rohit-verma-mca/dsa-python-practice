"""
Question:
Take an O(n) and an O(n^2) function, run each on lists of increasing
size (100, 1000, 5000, 10000), time each run, and print how the
runtime grows - proving the O(n^2) one slows down much faster.

Topic     : Complexity, Big-O
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""

import time
import random


def find_max(lst):
    max_value = lst[0]
    for item in lst:
        if item > max_value:
            max_value = item
    return max_value


def find_all_pairs(lst):
    pairs = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                pairs.append((lst[i], lst[j]))
    return pairs


def time_function(func, data):
    start = time.time()
    func(data)
    end = time.time()
    return end - start


def solve():
    sizes = [100, 1000, 5000, 10000]

    print(f"{'Size':<10}{'O(n) time':<15}{'O(n^2) time':<15}")
    for size in sizes:
        data = [random.randint(1, 1000) for _ in range(size)]

        linear_time = time_function(find_max, data)
        quadratic_time = time_function(find_all_pairs, data)

        print(f"{size:<10}{linear_time:<15.6f}{quadratic_time:<15.6f}")


if __name__ == "__main__":
    solve()