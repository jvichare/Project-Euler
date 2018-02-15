import math

def smallest_prime_factor(n):
    """
    This function finds the first factor of n from [2, n], which will always
    be prime due to some reason that I honestly can't quite figure out
    """
    assert n >= 2
    for i in range(2, int(math.sqrt(n)) + 1):  # The .sqrt() is used for the rangr
                                               # as if n = a*b, a OR b < sqrt(n)
        if n % i == 0:
            return i
    return n  # n itself is prime


def compute():
    n = 600851475143
    while True:
        p = smallest_prime_factor(n)
        if p < n:
            n = n // p
        else:
            return(str(n))
     

print(compute())
    