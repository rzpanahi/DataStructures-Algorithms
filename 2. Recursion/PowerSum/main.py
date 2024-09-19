"""
Power Sum - Let’s define a peculiar type of array in which each element is either an integer or another peculiar array. Assume that a peculiar array is never empty. Write a function that will take a peculiar array as its input and find the sum of its elements. If an array is an element in the peculiar array you have to convert it to it’s equivalent value so that you can sum it with the other elements. Equivalent value of an array is the sum of its elements raised to the number which represents how far nested it is. For e.g. [2,3[4,1,2]] = 2+3+ (4+1+2)^2
"""

def power_sum(array: list, depth = 1):
    _sum = 0
    for i in array:
        if type(i) != list:
           _sum += i
        else:
            _sum += power_sum(i, depth+1)

    return _sum**depth


import sys
print(sys.setrecursionlimit(2000))
def func(n):
    if n == 0:
        return 5

    if n % 2 == 0:
        return func(n - 1) - 21
    else:
        return func(n - 1) ** 2


n = int(input())

print(func(n))