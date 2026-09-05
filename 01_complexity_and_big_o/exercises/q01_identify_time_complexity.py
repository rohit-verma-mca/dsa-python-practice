"""
Question:
Write 3 small functions - one O(1) (returns the first element of a
list), one O(n) (loops through a list once to find the max), one
O(n^2) (nested loop comparing every pair of elements). Add a comment
above each stating its Big-O and why.

Topic     : Complexity, Big-O
Source    : freeCodeCamp DSA Course
Difficulty: Easy
"""


# O(1) - constant time: accesses one index directly, regardless of list size
def get_first_element(lst):
    return lst[0]


# O(n) - linear time: visits every element exactly once
def find_max(lst):
    max_value = lst[0]
    for item in lst:
        if item > max_value:
            max_value = item
    return max_value


# O(n^2) - quadratic time: for every element, loops through every other element
def find_all_pairs(lst):
    pairs = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j:
                pairs.append((lst[i], lst[j]))
    return pairs


if __name__ == "__main__":
    sample = [3, 7, 1, 9, 4]

    print("First element (O(1)):", get_first_element(sample))
    print("Max value (O(n)):", find_max(sample))
    print("All pairs (O(n^2)):", find_all_pairs(sample))