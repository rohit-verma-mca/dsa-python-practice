"""
Question:
Write a recursive function that returns the sum of the digits of a
non-negative integer (e.g., 1234 -> 1+2+3+4 = 10).

Topic     : Recursion
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


if __name__ == "__main__":
    print(sum_of_digits(1234))  # 10
    print(sum_of_digits(7))     # 7