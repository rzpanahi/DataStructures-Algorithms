# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


def permutations(array: list):
    def swap(pos1, pos2):
        array[pos1], array[pos2] = array[pos2], array[pos1]

    length = len(array)
    result = []

    def helper(index):
        # base case
        if index == length - 1:
            result.append(array[:])
            return

        # making the next choice
        for j in range(index, length):
            # proceeding in the algorithm
            swap(index, j)
            # array[index], array[j] = array[j], array[index]

            # recursive case
            helper(index + 1)

            # backtracking part
            swap(index, j)
            # array[index], array[j] = array[j], array[index]

    helper(0)
    return result
