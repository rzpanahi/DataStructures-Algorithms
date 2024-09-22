# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


def permutation(array: list):
    def swap(pos1: int, pos2: int):
        array[pos1], array[pos2] = array[pos2], array[pos1]

    length = len(array)
    result = []

    def helper(index):
        if index == length - 1:
            result.append(array.copy())
            return

        for j in range(index, length):
            if index == j or array[j] != array[index]:
                swap(index, j)
                helper(index + 1)
                swap(index, j)

    helper(0)
    return result


# Time: O(n * n!) => we copy the full array (n) n! times (which is number of all possible permutations)
# Space: O(n) => length of call stack is n at max
