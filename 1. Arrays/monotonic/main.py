# An array is monotonic if it is either monotone increasing or monotone decreasing.else
# An array is monotone increasing if all its elements from left to right are non-decreasing.
# An array is monotone decreasing if all  its elements from left to right are non-increasing.
# Given an integer array return true if the given array is monotonic, or false otherwise.


def isMonotonic(arr: list):
    if len(arr) == 0:
        return True

    length = len(arr)
    first = arr[0]
    last = arr[length - 1]

    if first < last:
        # arr must be non-decreasing
        for i in range(length - 2):
            if arr[i] > arr[i + 1]:
                return False
    elif first > last:
        # arr must be non-increasing
        for i in range(length - 2):
            if arr[i] < arr[i + 1]:
                return False
    else:
        # arr values must be the same
        for i in range(length - 2):
            if arr[i] != arr[i + 1]:
                return False

    return True


# Time : O(n)
# Space : O(1)
