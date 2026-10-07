"""
Question:
Given a list of numbers and a target sum, return the indices of the
two numbers that add up to the target, using a single pass with a
hash map (not a nested loop).

Topic     : Hashing
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([3, 2, 4], 6))        # [1, 2]