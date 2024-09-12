# You are given an array of Integers in which each subsequent value is not less than the previous value.
# Write a function that takes this array as an input and
# returns a new array with the squares of each number sorted in ascending order.



# 1
def sorted_squared(arr: list):
    squared_arr = list()

    for i, number in enumerate(arr):
        squared_arr[i] = number ** 2

    return squared_arr.sort()

# Time : O(nlogn)
# Space : O(n)



# 2
def sorted_squared2(arr: list):
    start = 0
    end = len(arr) - 1
    new_arr = [0] * len(arr)

    for k in reversed(range(len(arr))):
        square_start = arr[start] ** 2
        square_end = arr[end] ** 2

        if square_end > square_start:
            new_arr[k] = square_end

            end = end -1
        else:
            new_arr[k] = square_start

            start = start + 1

    return new_arr

# Time : O(n)
# Space : O(n)
