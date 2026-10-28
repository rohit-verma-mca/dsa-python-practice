"""
Question:
Rewrite the naive recursive Fibonacci from the Recursion topic using
memoization (a dictionary cache), then time both versions to show the
difference.

Topic     : Dynamic Programming, Memoization
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""

import time


def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def solve():
    n = 30

    start = time.time()
    result_naive = fib_naive(n)
    naive_time = time.time() - start

    start = time.time()
    result_memo = fib_memo(n)
    memo_time = time.time() - start

    print(f"fib({n}) naive:    {result_naive}  ({naive_time:.6f} sec)")
    print(f"fib({n}) memoized: {result_memo}  ({memo_time:.6f} sec)")
    print(f"fib(100) memoized: {fib_memo(100)}")  # 354224848179261915075


if __name__ == "__main__":
    solve()