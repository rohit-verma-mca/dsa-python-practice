"""
Question:
Given item weights, item values, and a bag capacity, find the maximum
total value you can carry, where each item can be taken at most once.

Topic     : Dynamic Programming, 2D Table
Source    : freeCodeCamp DSA Course
Difficulty: Hard
"""


def knapsack(weights, values, capacity):
    n = len(weights)
    # dp[i][w] = best value using the first i items with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]  # option 1: skip this item
            if weights[i - 1] <= w:  # option 2: take it, if it fits
                take = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                dp[i][w] = max(dp[i][w], take)

    return dp[n][capacity]


if __name__ == "__main__":
    print(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7))        # 9
    print(knapsack([10, 20, 30], [60, 100, 120], 50))     # 220