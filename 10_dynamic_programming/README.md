# Dynamic Programming

**Source:** freeCodeCamp DSA Course

## Concepts covered
- Overlapping sub-problems and why plain recursion can be wasteful
- Memoization (top-down): recursion plus a cache of answers already computed
- Tabulation (bottom-up): filling a table from the smallest sub-problem upward
- Recognizing a DP problem: "find the best/count the ways" where choices repeat
- Classic problems: Fibonacci, climbing stairs, coin change, knapsack, LCS

## My Notes
Naive recursive Fibonacci recomputes the same values over and over, which makes it
exponential. Storing each result the first time it's computed (memoization) drops it to
O(n). Bottom-up tabulation does the same thing without recursion, by building the
answer from the smallest case upward. Most DP problems come down to two questions:
what is the smallest version of this problem, and how does the answer for a bigger
version depend on the answers for smaller ones? Once I can write that relationship
(the recurrence), the code follows from it.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Fibonacci with Memoization | ⬜ |
| 2 | Climbing Stairs | ⬜ |
| 3 | House Robber | ⬜ |
| 4 | Coin Change (Minimum Coins) | ⬜ |
| 5 | 0/1 Knapsack | ⬜ |
| 6 | Longest Common Subsequence | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../EXERCISE_FORMAT.md).