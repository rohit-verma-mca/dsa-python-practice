# Sorting Algorithms

**Source:** freeCodeCamp DSA Course

## Concepts covered
- Bubble sort, selection sort, insertion sort — simple O(n²) approaches
- Merge sort — divide and conquer, O(n log n)
- Quick sort — partitioning, average O(n log n)
- Comparing algorithm performance empirically, not just theoretically

## My Notes
The simple sorts (bubble, selection, insertion) are easy to understand but all O(n²) —
fine for small lists, painful at scale. Merge sort splits the list in half recursively
until pieces are trivially sorted, then merges them back together in order — the
"divide and conquer" pattern. Quick sort picks a pivot and partitions everything around
it instead — usually faster in practice than merge sort despite similar average-case
complexity, though it can degrade to O(n²) in a bad worst case.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Implement Bubble Sort | ⬜ |
| 2 | Implement Selection Sort | ⬜ |
| 3 | Implement Insertion Sort | ⬜ |
| 4 | Implement Merge Sort | ⬜ |
| 5 | Implement Quick Sort | ⬜ |
| 6 | Compare All Sorting Algorithms | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../EXERCISE_FORMAT.md).