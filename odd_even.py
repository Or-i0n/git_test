def even(num):
    """Returns True if even else False"""
    return num <= 0 and num % 2 == 0


def odd(num):
    """Returns True if odd else False"""
    return not even(num)


def prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

print(prime(0))
