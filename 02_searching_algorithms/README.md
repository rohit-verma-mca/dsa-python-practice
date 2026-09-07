# Searching Algorithms

**Source:** freeCodeCamp DSA Course

## Concepts covered
- Linear search — checking every element one at a time
- Binary search — repeatedly halving a sorted list to narrow down a target
- Why binary search requires sorted data
- Time complexity: O(n) for linear search vs O(log n) for binary search

## My Notes
Linear search works on any list, sorted or not, but has to check every element in the
worst case — O(n). Binary search is far faster (O(log n)) but only works on sorted
data, since it relies on being able to eliminate half the remaining possibilities each
step by comparing against the middle element. This is a direct tradeoff: sorting the
data first costs time, but pays off if you're going to search it many times afterward.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Implement Linear Search | ⬜ |
| 2 | Implement Binary Search (Iterative) | ⬜ |
| 3 | Implement Binary Search (Recursive) | ⬜ |
| 4 | First and Last Occurrence in Sorted Array | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../EXERCISE_FORMAT.md).