"""
Question:
Given a list of money in each house along a street, find the maximum
total you can rob without robbing two adjacent houses.

Topic     : Dynamic Programming
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


def rob(houses):
    prev, curr = 0, 0  # best total up to two houses ago, and up to the last house

    for money in houses:
        prev, curr = curr, max(curr, prev + money)

    return curr


if __name__ == "__main__":
    print(rob([1, 2, 3, 1]))      # 4  (rob houses 1 and 3)
    print(rob([2, 7, 9, 3, 1]))   # 12 (rob houses 1, 3 and 5)
    print(rob([]))                # 0