"""
Question:
Given a list of strings, group the ones that are anagrams of each
other into lists, using a hash map keyed by each word's sorted
letters.

Topic     : Hashing, Strings
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


def group_anagrams(words):
    groups = {}
    for word in words:
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())


if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]