"""
Question:
Given a list of numbers, return all numbers that appear more than
once, using a hash set to track what's been seen.

Topic     : Hashing
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


if __name__ == "__main__":
    print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))  # [1, 2] (order may vary)