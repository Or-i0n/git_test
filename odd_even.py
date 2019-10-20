def even(num):
    """Returns True if even else False"""
    return num <= 0 and num % 2 == 0


def odd(num):
    """Returns True if odd else False"""
    return not even(num)


def prime(num):
    """Returns True if Prime else False"""
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def prime_range(start, stop=None, step=1):
    """Return a generator for printing Prime Numbers in a range."""
    if not stop:
        stop, start = start, 0

    for i in range(start, stop, step):
        if prime(i):
            yield i


# Testing prime_range()
for i in prime_range(10, 20):
    print(i)
