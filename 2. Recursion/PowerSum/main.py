"""
Power Sum - Let’s define a peculiar type of array in which each element is either an integer or another peculiar array. Assume that a peculiar array is never empty. Write a function that will take a peculiar array as its input and find the sum of its elements. If an array is an element in the peculiar array you have to convert it to it’s equivalent value so that you can sum it with the other elements. Equivalent value of an array is the sum of its elements raised to the number which represents how far nested it is. For e.g. [2,3[4,1,2]] = 2+3+ (4+1+2)^2
"""

import sys

# prevents stack overflow for call stack
print(sys.setrecursionlimit(2000))


def power_sum(array: list, depth=1):
    _sum = 0
    for i in array:
        if type(i) is list:
            _sum += power_sum(i, depth + 1)
        else:
            _sum += i

    return _sum**depth


# Time: O(n) => n is total number of elements + total number of arrays and sub-arrays
# Space: O(depth) => maximux depth of sub-arrays

