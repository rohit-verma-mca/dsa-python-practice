# Complexity & Big-O

**Source:** freeCodeCamp DSA Course

## Concepts covered
- What Big-O notation actually measures (worst-case growth rate, not exact speed)
- Common complexity classes: O(1), O(log n), O(n), O(n log n), O(n²)
- Time complexity vs space complexity
- Why nested loops usually mean O(n²)

## My Notes
Big-O describes how an algorithm's runtime grows as input size grows — it's about the
*shape* of the growth curve, not the exact number of seconds. An O(n) algorithm doing
one loop over the list will always beat an O(n²) one eventually, even if the O(n²) one
looks faster on tiny inputs — the crossover point is what matters, not small-scale
appearances.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Identify and Prove Time Complexity | ⬜ |
| 2 | Linear vs Quadratic Growth Comparison | ⬜ |
| 3 | Nested Loop Complexity Analysis | ⬜ |
| 4 | Time vs Space Tradeoff Demo | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../EXERCISE_FORMAT.md).