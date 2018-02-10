def compute():
    """
    This function calculates the sum of even fibonacci numbers before
    they reach 4,000,000
    """
    x = 1  # Setting the initial fibonacci numbers here
    y = 2
    ans = 0
    while x <= 4000000:
        if x % 2 == 0:
            ans += x
        x, y = y, (x + y)
    print(ans)


compute()
