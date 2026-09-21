"""
Question:
Write a recursive function that returns the nth Fibonacci number
(0, 1, 1, 2, 3, 5, 8, ...), using plain recursion without memoization.

Topic     : Recursion, Branching Recursion
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    for i in range(10):
        print(fibonacci(i), end=" ")   # 0 1 1 2 3 5 8 13 21 34
    print()