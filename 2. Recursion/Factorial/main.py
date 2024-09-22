def factorial(n: int):
    if n == 1:
        return 1

    return factorial(n - 1) * n


# Time: O(n)
# Space: O(n)
