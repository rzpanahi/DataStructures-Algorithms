"""
The tower of Hanoi is a famous puzzle where we have three rods and N disks. The objective of the puzzle is to move the entire stack to another rod. You are given the number of discs N. Initially, these discs are in the rod 1. You need to print all the steps of discs movement so that all the discs reach the 3rd rod. Also, you need to find the total moves.
"""


def tower_of_hanoi(n):
    if n == 1:
        return 1

    return tower_of_hanoi(n - 1) * 2 + 1


# Time: O(n)
# Space: O(n)

