# Hashing

**Source:** freeCodeCamp DSA Course

## Concepts covered
- What a hash function does and why dict lookups are O(1) on average
- Hash collisions and how they're handled internally
- Using dictionaries/sets as a problem-solving tool, not just storage
- The "frequency counting" pattern (counting occurrences with a dict)
- The "two-sum" style pattern (checking complements using a set)

## My Notes
A hash table converts a key into a number (its hash) that maps directly to a memory
slot, which is why lookup, insert, and delete are all O(1) on average — no scanning
needed, unlike a list. Python's `dict` and `set` are both hash tables under the hood.
A huge class of problems that look like they need nested loops (O(n²)) can actually be
solved in O(n) by trading some memory for a hash table that remembers what you've
already seen — the same tradeoff explored in the Big-O topic's duplicate-checking
exercise.

## Practice Questions
| # | Question | Status |
|---|----------|--------|
| 1 | Two Sum | ⬜ |
| 2 | First Non-Repeating Character | ⬜ |
| 3 | Group Anagrams | ⬜ |
| 4 | Find All Duplicates in a List | ⬜ |
| 5 | Longest Consecutive Sequence | ⬜ |

> Solved questions go in `exercises/` as `qXX_short_description.py`, following the format in [`EXERCISE_FORMAT.md`](../EXERCISE_FORMAT.md).