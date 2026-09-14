"""
Question:
Write a recursive function that calculates the factorial of a
non-negative integer n (n! = n * (n-1) * (n-2) * ... * 1, and 0! = 1).

Topic     : Recursion
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(5))   # 120
    print(factorial(0))   # 1