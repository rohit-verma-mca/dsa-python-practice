"""
Question:
Write two functions that solve the same problem (checking whether a
list contains duplicate values) using different approaches: one that
uses O(1) extra space but O(n^2) time (nested loop comparison), and
one that uses O(n) extra space but O(n) time (a set/hash lookup).
Demonstrate the time difference and explain the space tradeoff.

Topic     : Complexity, Big-O, Space Complexity
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""

import time
import random


# Time: O(n^2), Space: O(1) - no extra data structure used
def has_duplicates_nested_loop(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False


# Time: O(n), Space: O(n) - uses a set to remember seen values
def has_duplicates_using_set(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return True
        seen.add(item)
    return False


def solve():
    sizes = [100, 1000, 5000]

    print(f"{'Size':<10}{'Nested loop (O(n^2))':<25}{'Set lookup (O(n))':<20}")
    for size in sizes:
        data = [random.randint(1, size * 10) for _ in range(size)]

        start = time.time()
        has_duplicates_nested_loop(data)
        t1 = time.time() - start

        start = time.time()
        has_duplicates_using_set(data)
        t2 = time.time() - start

        print(f"{size:<10}{t1:<25.6f}{t2:<20.6f}")

    print("\nTradeoff: the set-based version is much faster, but it uses extra")
    print("memory to store seen values. The nested loop version uses no extra")
    print("memory, but pays for that with much slower runtime on large lists.")


if __name__ == "__main__":
    solve()