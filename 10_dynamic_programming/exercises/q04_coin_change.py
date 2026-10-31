"""
Question:
Given a list of coin denominations and a target amount, return the
fewest coins needed to make that amount, or -1 if it can't be made.

Topic     : Dynamic Programming, Tabulation
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


def coin_change(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0  # zero coins needed to make amount 0

    for current in range(1, amount + 1):
        for coin in coins:
            if coin <= current and dp[current - coin] + 1 < dp[current]:
                dp[current] = dp[current - coin] + 1

    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    print(coin_change([1, 2, 5], 11))  # 3  (5 + 5 + 1)
    print(coin_change([2], 3))         # -1
    print(coin_change([1], 0))         # 0