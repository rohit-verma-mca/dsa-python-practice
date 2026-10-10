"""
Question:
Given an unsorted list of integers, find the length of the longest
run of consecutive integers (e.g., [100, 4, 200, 1, 3, 2] -> the
sequence 1,2,3,4 has length 4), using a hash set for O(n) time
instead of sorting first.

Topic     : Hashing
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # only start counting from the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            longest = max(longest, current_length)

    return longest


if __name__ == "__main__":
    print(longest_consecutive_sequence([100, 4, 200, 1, 3, 2]))  # 4
    print(longest_consecutive_sequence([]))                       # 0