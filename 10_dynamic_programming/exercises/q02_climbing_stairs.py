"""
Question:
You can climb a staircase of n steps taking either 1 or 2 steps at a
time. Write a function that returns how many distinct ways there are
to reach the top, using bottom-up DP.

Topic     : Dynamic Programming, Tabulation
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


def climb_stairs(n):
    if n <= 2:
        return n

    prev, curr = 1, 2  # ways to reach step 1 and step 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr

    return curr


if __name__ == "__main__":
    print(climb_stairs(1))   # 1
    print(climb_stairs(3))   # 3
    print(climb_stairs(5))   # 8
    print(climb_stairs(10))  # 89