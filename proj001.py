def compute(n):
    """
    Function that returns the sum of all numbers divisible by 3 or 5
    up to a specified number, n
    """
    ans = sum(x for x in range(n) if (x % 3 == 0 or x % 5 == 0))
    print(ans)


compute(1000)
