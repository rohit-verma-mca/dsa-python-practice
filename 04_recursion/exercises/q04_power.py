"""
Question:
Write a recursive function that calculates x raised to the power n
(x^n), for a non-negative integer n.

Topic     : Recursion
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)


if __name__ == "__main__":
    print(power(2, 10))  # 1024
    print(power(5, 0))   # 1