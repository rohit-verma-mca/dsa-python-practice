"""
Question:
Given three different functions using nested loops, determine and
prove the time complexity of each: one with two independent nested
loops (O(n^2)), one with a nested loop that shrinks each iteration
(still O(n^2) but half the work), and one with three nested loops
(O(n^3)).

Topic     : Complexity, Big-O
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""

import time
import random


# O(n^2) - two independent loops, full range each time
def print_all_pairs(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count


# Still O(n^2) - inner loop shrinks, but total work is still proportional to n^2
# (roughly half the operations of the version above, but same growth shape)
def print_triangular_pairs(n):
    count = 0
    for i in range(n):
        for j in range(i, n):
            count += 1
    return count


# O(n^3) - three nested loops, each running the full range
def print_all_triples(n):
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1
    return count


def solve():
    sizes = [10, 20, 40, 80]

    print(f"{'Size':<10}{'O(n^2) full':<15}{'O(n^2) triangular':<20}{'O(n^3)':<15}")
    for n in sizes:
        start = time.time()
        print_all_pairs(n)
        t1 = time.time() - start

        start = time.time()
        print_triangular_pairs(n)
        t2 = time.time() - start

        start = time.time()
        print_all_triples(n)
        t3 = time.time() - start

        print(f"{n:<10}{t1:<15.6f}{t2:<20.6f}{t3:<15.6f}")


if __name__ == "__main__":
    solve()