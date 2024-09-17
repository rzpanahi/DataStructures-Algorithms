# from 0 no n
def fibonacci(m, n):
    if m == n:
        return n

    return m + fibonacci(m + 1, n)


# from n to 0
def fibonacci2(n):
    if n == 1:
        return 1

    return n + fibonacci2(n - 1)