def myPow(a: int, b: int) -> int:
    """
    Multiply intermediate value by itself until we can't any more, doubling
    accumulated power 'c' by 2. When we can't double c, recursively call
    this method with remainder.

    Time:
    - O(lg(b))

    Space:
    - O(1)

    >>> myPow(3, 4) == 3**4
    True
    >>> myPow(-3, 4) == (-3)**4
    True
    >>> myPow(4, 5) == 4**5
    True
    >>> myPow(-4, 5) == (-4)**5
    True
    >>> myPow(5, 12) == 5**12
    True
    """
    c = 1
    value = a
    while c < b:
        if c * 2 <= b:
            value *= value
            c *= 2
        else:
            value *= myPow(a, b - c)
            c = b
    return value

if __name__ == '__main__':
    import doctest
    doctest.testmod()
