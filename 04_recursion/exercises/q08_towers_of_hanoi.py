"""
Question:
Write a recursive function that solves the classic Towers of Hanoi
puzzle - move n disks from a source rod to a destination rod, using
an auxiliary rod, following the rule that a larger disk can never sit
on top of a smaller one. Print each move made.

Topic     : Recursion, Classic Problem
Source    : freeCodeCamp DSA Course
Difficulty: Medium
"""


def solve_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    solve_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    solve_hanoi(n - 1, auxiliary, source, destination)


if __name__ == "__main__":
    solve_hanoi(3, "A", "B", "C")
    # Moves 3 disks from rod A to rod C, using rod B, in the minimum
    # number of moves (7 moves for 3 disks)