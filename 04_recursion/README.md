# Recursion

**Source:** freeCodeCamp DSA Course

## Concepts covered
- Base case vs recursive case
- The call stack — how recursive calls stack up and unwind
- Recursion vs iteration (when each is more natural)
- Multiple recursive calls (branching recursion) vs single recursive calls
- Classic recursion problems: factorial, Fibonacci, Towers of Hanoi

## My Notes
Every recursive function needs a base case (a condition that stops the recursion) and a
recursive case (where it calls itself with a smaller version of the problem) — without
a solid base case, it recurses forever until Python hits its recursion limit and crashes.
Recursion mirrors how you'd describe a problem in plain English sometimes ("factorial of
n is n times factorial of n-1") more naturally than a loop would. Branching recursion
(like Fibonacci, which calls itself twice per call) can get slow fast without
optimization, since the same sub-problems get recalculated repeatedly.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Factorial | ⬜ |
| 2 | Fibonacci (Naive Recursive) | ⬜ |
| 3 | Sum of Digits | ⬜ |
| 4 | Power / Exponentiation | ⬜ |
| 5 | Reverse a String | ⬜ |
| 6 | Palindrome Check | ⬜ |
| 7 | Sum of a List | ⬜ |
| 8 | Towers of Hanoi | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../EXERCISE_FORMAT.md).