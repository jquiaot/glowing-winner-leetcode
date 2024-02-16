import math

"""
A positive integer is considered uniform if all of its digits are equal. For
example, 222222 is uniform, while 223223 is not.

Given two positive integers AA and BB, determine the number of uniform integers
between AA and BB, inclusive.

Please take care to write a solution which runs within the time limit.

Discussion:

Intuitively, there can be at most 9 uniform integers with a certain number
of digits, i.e., for 2-digit numbers, the uniform integers are
[11, 22, ...,99].

So what we need to do then is:
- Figure out the number of digits needed for A => aDigits
- Figure out the number of digits needed for B => bDigits
- For number of digits from aDigits-bDigits
  - Generate uniform numbers for that number of digits
  - Accept uniform number if n >= A and n <= B

Time:
- Something like O(n) where n is the difference between the number
  of digits between A and B?
  - e.g. digitsA=2, digitsB=4 => at most (4-2+1)*9 = 27 numbers
  - e.g. digitsA=1, digitsB=5 => at most (5-1+1)*9 = 54 numbers
Space:
- => O(1) constant time for storing number of digits the uniform numbers
     should be, and the total number of uniform digits calculated
"""
def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    """
    >>> getUniformIntegerCountInInterval(75, 300)
    5
    >>> getUniformIntegerCountInInterval(1, 9)
    9
    >>> getUniformIntegerCountInInterval(999999999999, 999999999999)
    1
    >>> getUniformIntegerCountInInterval(11, 11)
    1
    >>> getUniformIntegerCountInInterval(11, 99)
    9
    >>> getUniformIntegerCountInInterval(11, 999)
    18
    """
    aDigits = int(math.floor(math.log10(A))) + 1
    bDigits = int(math.floor(math.log10(B))) + 1

    total = 0
    for numDigits in range(aDigits, bDigits + 1):
        if numDigits > aDigits and numDigits < bDigits:
            # we don't need to calculate uniform numbers for this number
            # of digits since there's no overlap between A and B
            total += 9
        else:
            # possible overlap between A and B, so need to calculate
            total += getUniformIntCount(A, B, numDigits)
    return total

def getUniformIntCount(A: int, B: int, numDigits: int) -> int:
    cur = int('1' * numDigits)
    increment = cur

    count = 0
    for i in range(9): # do this at most 9 times
        if cur < A:
            # current value less than A, so don't count it
            cur += increment
            continue
        elif cur > B:
            # current value if greater than B, so we're done
            break
        else:
            # add to cur to get to next uniform num, and increment count
            cur += increment
            count += 1
    return count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
